"""
TABELAS

Todas as tabelas do capítulo Personagens colocados em Tuplas e Dicionários

"""


racas = ('Humano', 'Meio-Elfo', 'Elfo-Florestal', 'Elfo-Dourado', 'Anão', 'Pequenino')

profissao = (('Guerreiro', True, True, True, True, True, True),
             ('Ladino', True, True, True, True, True, True),
             ('Sacerdote', True, True, True, True, True, True),
             ('Mago', True, True, True, True, False, False),
             ('Rastreador', True, True, True, True, False, False),
             ('Bardo', True, True, True, True, False, False))

deuses = {'Sevides': 'agricultura, fertilidade',
          'Quiris': 'plantio',
          'Liris': 'colheita',
          'Ganis': 'água, mar',
          'Blator': 'guerra',
          'Crisagon': 'honra, estratégia, bravura',
          'Crezir': 'fúria, matança, prazer da luta',
          'Maira mon': 'natureza em aspecto mineral',
          'Maira vet': 'natureza em aspcto vegetal',
          'Maira nil': 'natureza em aspecto animal',
          'Selimon': 'paz,amor',
          'Lena': 'prazer erótico e praer no trabalho',
          'Plandis': 'paixão cega, loucura, inconsequência',
          'Cambu': 'diplomacia, comércio, interrelações',
          'Cruine': 'morte, protetor das almas, reencarnação',
          'Palier': 'conhecimento, magia',
          'Parom': 'artífices'}

equipamentos = {'Guerreiro': ('armadura de couro leve', 'escudo pequeno'),
                'Ladino': ('manto com capuz', 'escudo pequeno', 'corda 20 metros'),
                'Sacerdote': ('manto com capuz', 'símbolo sagrado de ferro', 'água abençoada', 'cinto', 'pederneiras', 'mochila'),
                'Mago': ('manto com capuz', 'pena e tinta', 'pergaminho', 'cinto', 'pederneiras', 'mochila'),
                'Rastreador': ('armadura de couro leve', 'capa', 'par de luvas', 'cinto', 'pederneiras'),
                'Bardo': ('instrumento musical', 'capa', 'par de botas', 'cinto', 'mochila')}

ajuste_atri_raca = {'intelecto': (0, 0, 1, 1, 0, 0),
                    'aura': (0, 0, 0, 1, -1, 0),
                    'carisma': (0, 1, 0, 1, 0, 0),
                    'força': (0, 0, 0, -1, 1, -2),
                    'físico': (0, 0, -1, -1, 2, 1),
                    'agilildade': (0, 0, 1, 1, -1, 2),
                    'percepção': (0, 0, 1, 0, 0, 1)}

velocidade = {'Humano': 18, 'Meio-Elfo': 17, 'Elfo-Florestal': 16, 'Elfo-Dourado': 16, 'Anão': 14, 'Pequenino': 12}

equipamento_defesa = {'nada': ('Leve', 'L', 0, 0),
                      'couro leve': ('Leve', 'L', 1, 3),
                      'couro rígido': ('Médio', 'M', 0, 6),
                      'cota de malha parcial': ('Médio', 'M', 1, 9),
                      'cota de malha completa': ('Pesada', 'P', 0, 12),
                      'couraça metálica parcial': ('Pesada', 'P', 1, 15),
                      'escudo pequeno': ('', '', 1, 3),
                      'escudo grande': ('', '', 1, 5),
                      'elmo aberto': ('', '', 0, 1),
                      'elmo fechado': ('', '', 0, 2)}

ef_basica = {'Humano': 15, 'Meio-Elfo': 13, 'Elfo-Florestal': 12, 'Elfo-Dourado': 12, 'Anão': 12, 'Pequenino': 11}

eh_basica = {'Guerreiro': 18, 'Ladino': 12, 'Sacerdote': 12, 'Mago': 6, 'Rastreador': 15, 'Bardo': 9}

