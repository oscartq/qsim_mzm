# from qiskit_nature.operators.second_quantization import FermionicOp
# from qiskit_nature.mappers.second_quantization import JordanWignerMapper

# def compute_H_secondquant(eps, t, tc, delta, num_sites):

#     second_quant_H = 0
#     for i in range(num_sites):
#         second_quant_H += eps[i] * FermionicOp("+_{}".format(i)) @ FermionicOp("-_{}".format(i))

#         if i % 2 == 0 and i + 1 < num_sites:
#             second_quant_H += t*(FermionicOp("+_{}".format(i)) @ FermionicOp("-_{}".format(i + 1)) + FermionicOp("+_{}".format(i+1)) @ FermionicOp("-_{}".format(i)) )
#             second_quant_H += delta*(FermionicOp("+_{}".format(i)) @ FermionicOp("+_{}".format(i + 1)) + FermionicOp("-_{}".format(i + 1)) @ FermionicOp("-_{}".format(i)) )
        
#         elif i % 2 == 1 and i + 1 < num_sites:
#             second_quant_H += tc*(FermionicOp("+_{}".format(i)) @ FermionicOp("-_{}".format(i + 1)) + FermionicOp("+_{}".format(i+1)) @ FermionicOp("-_{}".format(i)) )

#     # Transform to Pauli Operators
#     jw_mapper = JordanWignerMapper
#     pauli_H = JordanWignerMapper.map(jw_mapper, second_quant_H)

#     return pauli_H

# # Example computation
# H = compute_H_secondquant(eps, 1, 0.5, 1, num_sites)
# H