scoring = {
"parameters":
   {'smiles_file': 'compounds.smi', 'output_csv': 'scoring.csv', 'smiles_column': 'SMILES', 'standardize_smiles': True 
   },
"scoring":
   {"type": "geometric_mean", "parallel": False,
   "component":
       [
           {"custom_alerts":
                {"endpoint":
                    {"name": "Alerts", "params":
                        {"smarts":
                             [
                             "[*;r8]", "[*;r9]", "[*;r10]", "[*;r11]", "[*;r12]", "[*;r13]", "[*;r14]", "[*;r15]", "[*;r16]", "[*;r17]", "[#8][#8]", "[#6;+]", "[#16][#16]", "[#7;!n][S;!$(S(=O)=O)]", "[#7;!n][#7;!n]", "C#C", "C(=[O,S])[O,S]", "[#7;!n][C;!$(C(=[O,N])[N,O])][#16;!s]", "[#7;!n][C;!$(C(=[O,N])[N,O])][#7;!n]", "[#7;!n][C;!$(C(=[O,N])[N,O])][#8;!o]", "[#8;!o][C;!$(C(=[O,N])[N,O])][#16;!s]", "[#8;!o][C;!$(C(=[O,N])[N,O])][#8;!o]", "[#16;!s][C;!$(C(=[O,N])[N,O])][#16;!s]"
                             ]
                         }
                    }
                }
            },
            {"QED":
                {"endpoint":
                    {"name": "QED", "weight": 0.25}
                }
            },
            {"MolecularWeight":
                {"endpoint":
                    {"name": "MW", "weight": 0.25, "transform":
                       {"type": "double_sigmoid", "high": 500.0, "low": 200.0, "coef_div": 500.0, "coef_si": 20.0, "coef_se": 20.0
                       }
                    }
                }
            },
            {"TanimotoDistance":
                {"endpoint":
                    {"name": "Tanimoto similarity ECF6", "weight": 0.1, "params":
                        {"smiles":
                             "n1(nc(c(c1C)-c2n{nH}c(c2){C@@}3({C@@H}(CN(CC3)Cc4nc5c(c(n4)C)cccc5)O)OC)C)C",
                             "radius": 3, "use_counts": True, "use_features": True
                        }
                    }
                }
            },

         {
            "pmi":{
               "endpoint":[
                  {
                     "name":"PMI 3D-likeness",
                     "weight":0.79,
                     "params":{
                        "property":"npr1"
                              }
                  },
                  {
                     "weight":0.21,
                     "params":{
                        "property":"npr2"
                              }
                  }
               ]
            }
         }
      ]
   }
}
