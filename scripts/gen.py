import sys
from pyneuroml.pynml import run_lems_with_jneuroml, print_comment_v, read_neuroml2_file, extract_annotations
import csv

# ofile  = open('ttest.csv', "wb")
# writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)
#
# for row in reader:
#     writer.writerow(row)
#
# ifile.close()
# ofile.close()


def get_channels_from_channel_file(channel_file):
    doc = read_neuroml2_file(channel_file, include_includes=True, verbose=False, already_included=[])
    channels = list(doc.ion_channel_hhs.__iter__()) + \
               list(doc.ion_channel.__iter__())
    return channels


def get_channel_gates(channel):
    channel_gates = []
    for gates in ['gates','gate_hh_rates','gate_hh_tau_infs', 'gate_hh_instantaneouses']:
        if hasattr(channel,gates):
            for g in getattr(channel,gates):
                channel_gates += [(gates,g.id)]
        else:
            channel_gates += [(gates,'')]
    return channel_gates

def get_conductance_expression(channel):
    expr = 'g = gmax '
    for gates in ['gates','gate_hh_rates','gate_hh_tau_infs', 'gate_hh_instantaneouses']:
        for g in getattr(channel,gates):
            instances = int(g.instances)
            expr += '* %s<sup>%s</sup> '%(g.id, g.instances) if instances >1 else '* %s '%(g.id)
    return expr

def get_annotations(channel_file):
    print "here"
    print channel_file
    print extract_annotations(channel_file)

def driver():
    channel_file = sys.argv[1]
    tname=channel_file.split('.')
    csv_filename=tname[0]
    print csv_filename
    get_annotations(channel_file)
    chfile  = open(csv_filename+'.csv', "wb")
    writer = csv.writer(chfile)
    row=['channel_id','channel_species','channel_conductance','gate_type', 'gate_id']
    writer.writerow(row)
    channels = get_channels_from_channel_file(channel_file)
    print "*** CHANNELS ***"
    for channel in channels:
        row=[]
        row.append(channel.id)
        row.append(channel.species)
        row.append(channel.conductance)
        gates = get_channel_gates(channel)
        for g in gates:
            writer.writerow(row+[g[0],g[1]])
    chfile.close()
driver()
