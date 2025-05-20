from qiskit.opflow import I, X, Y, Z # type: ignore
from qiskit_nature.operators.second_quantization import FermionicOp # type: ignore
from qiskit_nature.mappers.second_quantization import JordanWignerMapper # type: ignore

#Parity operator
def p_op(num_sites):
    p_op = [ 
        (I ^ i) ^ Z ^ (I ^ (num_sites - i - 1))
        for i in range(num_sites)
    ]
    return p_op

#Number operator
def n_op(num_sites):
    n_is = [
    1 / 2 * ((I ^ num_sites) - ((I ^ i) ^ Z ^ (I ^ (num_sites - i - 1))))
    for i in range(num_sites)
    ]
    return n_is

def corr_op(num_sites, site1, site2):
    corr=FermionicOp("-_"+str(site1), register_length = num_sites)@FermionicOp("-_"+str(site2), register_length = num_sites)

    jw_mapper = JordanWignerMapper
    corr_JW = [JordanWignerMapper.map(jw_mapper, corr)]

    return corr_JW

def corr_dagger_op(num_sites, site1, site2):
    corr=FermionicOp("+_"+str(site1), register_length = num_sites)@FermionicOp("+_"+str(site2), register_length = num_sites)

    jw_mapper = JordanWignerMapper
    corr_JW = [JordanWignerMapper.map(jw_mapper, corr)]
    
    return corr_JW

def cc_site_op(num_sites):
    cc_op = [
        0.0 * (I ^ num_sites)
    ]
    return cc_op

def cc_nb_op(num_sites, site1, site2):
    if abs(site1 - site2) != 1:
        raise ValueError('Error: Sites have to be nearest neighbour sites. Use corr_op for other sites.')
    
    sigma_plus = 0.5*(X + 1.0j*Y)
    if site1 < site2:
        cc_op = [ 
            (I ^ site1) ^ -sigma_plus ^ sigma_plus ^ (I ^ (num_sites - site1 - 2)) 
        ]
    elif site1 > site2:
        cc_op = [
            (I ^ site2) ^ sigma_plus ^ sigma_plus ^ (I ^ (num_sites - site2 - 2)) 
        ]

    return cc_op

def cc_edge_op(num_sites, site1, site2):
    sigma_plus = 0.5*(X + 1.0j*Y)
    if site1 < site2:
        cc_op = [
            sigma_plus ^ (Z ^ (num_sites - 2)) ^ -sigma_plus
        ]
    elif site1 > site2:
        cc_op = [
            sigma_plus ^ (Z ^ (num_sites - 2)) ^ sigma_plus
        ]
            
    return cc_op

# corr=\
#     FermionicOp("+_0", register_length = nqbit)@FermionicOp("+_"+str(nqbit-1), register_length = nqbit)\
#     +FermionicOp("-_0", register_length = nqbit)@FermionicOp("+_"+str(nqbit-1), register_length = nqbit)\
#     -FermionicOp("+_0", register_length = nqbit)@FermionicOp("-_"+str(nqbit-1), register_length = nqbit)\
#     -FermionicOp("-_0", register_length = nqbit)@FermionicOp("-_"+str(nqbit-1), register_length = nqbit)

# #Correlation operator
# nqbit = num_sites
# parity_op=FermionicOp("-_1", register_length = nqbit)@FermionicOp("-_0", register_length = nqbit)

# jw_mapper = JordanWignerMapper
# parity_op_JW = JordanWignerMapper.map(jw_mapper, parity_op)
# parity_op_JW