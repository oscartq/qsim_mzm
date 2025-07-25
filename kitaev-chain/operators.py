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
    n_op_JW = []
    for i in range(num_sites):
        n_op = FermionicOp("+_"+str(i), register_length = num_sites) @ FermionicOp("-_"+str(i), register_length = num_sites)
        jw_mapper = JordanWignerMapper
        n_op_JW.append(JordanWignerMapper.map(jw_mapper, n_op))
    
    return n_op_JW

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

def gamma_corr_op(num_sites, siteA, siteB):
    gamma_corr_1 = FermionicOp("-_"+str(siteA), register_length = num_sites) + FermionicOp("+_"+str(siteA), register_length = num_sites)
    gamma_corr_2 = 1.0j * (FermionicOp("+_"+str(siteB), register_length = num_sites) - FermionicOp("-_"+str(siteB), register_length = num_sites))
    gamma_corr = gamma_corr_1 @ gamma_corr_2

    jw_mapper = JordanWignerMapper
    gamma_corr_JW = [JordanWignerMapper.map(jw_mapper, gamma_corr)]

    return gamma_corr_JW 

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