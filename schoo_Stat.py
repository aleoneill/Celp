# school_info = {
#     'California State Monterey Bay' : { 
#             'total_admitted':15561,
#             'total_accepted':7576,
#             'accept_perc': (7576 / 15561),
#             'St_Ratio_Fac': 22,
#             'In_cost': 5963.00,
#             'Out_cost': 17123.00
        
#     },
#     'San Diego State University': { 
#             'total_admitted':59051,
#             'total_accepted':20321,
#             'accept_perc': (20321 / 59051),
#             'St_Ratio_Fac': 28,
#             'In_cost': 6578.00,
#             'Out_cost': 17738.00
        
#     },
#     'San Jose State University': { 
#             'total_admitted':30584,
#             'total_accepted':16890,
#             'accept_perc': (16890 / 30584),
#             'St_Ratio_Fac': 27,
#             'In_cost': 6852.00,
#             'Out_cost': 18012.00
        
#     },
#     'University of California Irvine':{ 
#             'total_admitted':71775,
#             'total_accepted':27764,
#             'accept_perc': (27764 / 71775),
#             'St_Ratio_Fac': 19,
#             'In_cost': 13122.00,
#             'Out_cost':36000.00
        
#     },
#     'University of California Berkeley':{ 
#             'total_admitted':78893,
#             'total_accepted':13320,
#             'accept_perc': (13320 / 78893),
#             'St_Ratio_Fac': 17,
#             'In_cost': 12874.00,
#             'Out_cost':35752.00
        
#     },
#     'University of California Davis': { 
#             'total_admitted':64602,
#             'total_accepted':24518,
#             'accept_perc': (24518 / 64602),
#             'St_Ratio_Fac': 18,
#             'In_cost': 13877.00,
#             'Out_cost':36755.00},
# }

# put in function with colleges as argument

# colleges[collegename]['data'] = 

def statistics(colleges):
    colleges['UC Berkeley']['data'] = {
        'total_admitted':78893,
        'total_accepted':13320,
        'accept_perc': 16,
        'St_Ratio_Fac': 17,
        'In_cost': 12874.00,
        'Out_cost':35752.00
    }
    colleges['UC Davis']['data'] = { 
        'total_admitted':64602,
        'total_accepted':24518,
        'accept_perc': 38,
        'St_Ratio_Fac': 18,
        'In_cost': 13877.00,
        'Out_cost':36755.00
    }
    colleges['UC Irvine']['data'] = { 
        'total_admitted':71775,
        'total_accepted':27764,
        'accept_perc': 38,
        'St_Ratio_Fac': 19,
        'In_cost': 13122.00,
        'Out_cost':36000.00
        
    }
    colleges['San Jose State']['data'] = { 
        'total_admitted':30584,
        'total_accepted':16890,
        'accept_perc': 55,
        'St_Ratio_Fac': 27,
        'In_cost': 6852.00,
        'Out_cost': 18012.00
    }
    colleges['San Diego State']['data'] = { 
        'total_admitted':59051,
        'total_accepted':20321,
        'accept_perc': 34,
        'St_Ratio_Fac': 28,
        'In_cost': 6578.00,
        'Out_cost': 17738.00
    }
    colleges['CSU Monterey Bay']['data'] = { 
        'total_admitted':15561,
        'total_accepted':7576,
        'accept_perc': 48,
        'St_Ratio_Fac': 22,
        'In_cost': 5963.00,
        'Out_cost': 17123.00
    }
    
    return colleges