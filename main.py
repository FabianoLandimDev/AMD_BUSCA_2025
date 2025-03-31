from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


# Nome_do _programa: AMD_BUSCA
#
# site: https://github.com/FabianoLandimDev/AMD_BUSCA_2025
#
# Autor: Fabiano Landim <landimfabiano01@gmail.com>
#
# Manutenção: Fabiano Landim <landimfabiano01@gmail.com>
#
# ESCOPO:
# O Programa consiste em uma Interface Gráfica, desenvolvida com a Biblioteca do Python (PysimpleGUI),
# o intuito do mesmo é auxiliar os operadores lotados no Balcão de Informações do TRJFA (AMD-SERVICES), que necessitam de dados sobre as Empresas no TRJFA-MG.
#
# Histórico:
#
# v1.0.0_2022-08-14, Fabiano Landim:
# - Versão Inicial do Programa.
#
# v1.0.1_2023-05-10, Fabiano Landim:
# - Versão Inicial do Programa, com alguns ajustes ortográficos para facilitar a digitação nas pesquisas pelos colaboradores (usuário final) além do recurso de confirmar a pesquisa com a tecla enter do teclado da Máquina (PC/NOTEBOOK).
#
# - Versão Inicial do Programa, com alguns ajustes ortográficos. Atualização de busca sobre o estabelecimento Farmácia FARMACIAKI, que se desligara do TRJDF em outubro de 2023
#
# v1.0.2_2024-01-22, Fabiano Landim:
# - Mudanças em algumas linhas do código, referente algumas lojas que foram desligadas do TRJFA, inclusão de algumas novas informações sobre guichês no interior do terminal.
#
#v1.0.3_2024-03-07, Fabiano Landim
# - Acréscimo de duas novas cidades, Miguel Pereira, e Pernambuco, Empresas UTIL, PROGRESSO e PARAIBUNA.
#
# v1.0.4_2024-08-13, Fabiano Landim
# - Correçõe dos novos números de telefone do balcão de informações, inclusão de novos serviços.
#
# v1.0.5_2024_10_10, Fabiano Landim
# - Atualização de dados pertinentes à alguns números de telefone de algumas Empresas de Ônibus lotadas no TRJF
# Licença: MIT.
#
#
# v1.0.6_2025_03_31, Fabiano Landim
# - Foram realizadas mudanças significativas no Programa, nessa versão em diante o mesmo funcionará na biblioteca kivy do Python, sendo assim houveram mudanças no Layout.
# Licença: MIT
#
##############################################################################################################################################################################
# 
#
# LISTA DE CIDADES POR EMPRESAS:
#
# VIAÇÃO PROGRESSO:
#
cidade_4 = ['afonso arinos', 'além paraíba', 'alem paraiba', 'além paraiba', 'alem paraíba', 'barra mansa', 'barra do piraí', 'barra do pirai', 'levy gasparian', 'matias barbosa', 'miguel pereira', 'miracema', 'paraíba do sul', 'paraiba do sul', 'pirapitinga', 'serraria', 'três rios', 'tres rios', '3 rios', 'vassouras', 'volta redonda']
#
# VIAÇÃO SARITUR / COORDENADAS:
#
cidade_1 = ['bh', 'belo horizonte', 'betim', 'carandaí', 'congonhas', 'conselheiro lafayete', 'barbacena', 'congonhas', 'contagem', 'itaúna', 'mariana', 'natal', 'ouro preto', 'pará de minas', 'raposo', 'ressaquinha']
#
# VIAÇÃO UTIL/ BRISA/ SAMPAIO:
#
cidade_2 = ['angra dos reis', 'brasília', 'caxias', 'conservatória', 'goiânia - "util"', 'goiania - "util"', 'gurupí - "util"', 'imperatriz', 'macaé', 'macae', 'madureira', 'rio de janeiro', 'rj', 'valença', 'valenca', 'manoel duarte', 'mogi das cruzes', 'niterói', 'niteroi', 'ouro branco', 'parati', 'pernambuco', 'rio das flores', 'rio das ostras - próximo secretaria de turismo', 'são bernardo do campo', 'sao bernardo do campo', 'são josé dos campos - "util"', 'sao jose dos campos - "util"', 'taubaté', 'valença', 'valenca']
#
# VIAÇÃO UNIDA:
#
cidade_5 = ['caranguejo', 'coimbra', 'coronel fabriciano', 'ervália', 'ervalia', 'ipatinga', 'itabira', 'joão molevade', 'joao molevade', 'molevade',  'mercês', 'merces', 'nova era', 'ponte nova', 'porto firme', 'rio casca', 'rio pomba', 'são domingos do prata', 'sao domingos do prata', 'sddp', 'são geraldo', 'sao geraldo', 'senador firmino', 'tabuleiro', 'teixeiras', 'timóteo', 'timoteo', 'tocantins', 'ubá', 'uba', 'viçosa', 'vicosa', 'visconde do rio branco']
#
# VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001:
#
cidade_3 = ['alfenas - "cometa"', 'águas de lindóia', 'aguas de lindoia', 'americana', 'aparecida do norte', 'bragança paulista', 'campinas', 'campo mourão', 'campo mourao', 'são paulo - "cometa"', 'sao paulo - cometa', 'araraquara', 'catanduvas', 'curitiba', 'extrema', 'florianópolis',  'florianopolis', 'floripa', 'jacareí', 'jacarei', 'joinvile', 'jundiaí', 'jundiai', 'londrina', 'medianeira', 'mogi mirim', 'mogi guaçu', 'mogi guaçú', 'mogi guacu', 'ourinhos', 'piracicaba', 'pirassununga', 'porto alegre', 'resende', 'ribeirão preto - "cometa"', 'ribeirao preto - "cometa"', 'santo andré', 'santo andre', 'santos', 'são caetano', 'sao caetano', 'são carlos', 'sao carlos', 'são gonçalo do sapucaia', 'sao gonçalo do sapucaia', 'são joão do rio preto', 'sao joao do rio preto', 'sorocaba']
#
# VIAÇÃO TRANSUR:
#
cidade_6 = ['bananal', 'barbacena', 'barroso', 'caieiro', 'correia de almeida', 'dores de campos', 'ewbank da câmara', 'ewbank da camara', 'faixa azul', 'helvas', 'ibertioga', 'itutinga', 'lavras', 'madre de deus', 'peróbas', 'perobas', 'prados', 'santos dumont', 'são joão da serra', 'sao joao da serra', 'são joão del rei', 'sao joao del rei', 'são sebastião da vitória', 'sao sebastiao da vitoria', 'tiradentes']
#
# VIAÇÃO BASSAMAR:
#
cidade_7 = ['aeroporto - "bassamar"', 'acampamento de campelina', 'andrelândia', 'arantina', 'argirita - conexão', 'bela vista de minas', 'bias fortes', 'bicas', 'boa vista', 'bom jardim de minas - conexão', 'br 267 - guarará - conexão', 'cachoeira', 'chiador', 'conceição', 'conceição do rio verde', 'conceicao do rio verde', 'conceiçao do rio verde', 'conceição do monte alegre - "bassamar"', 'coronel pacheco - conexão', 'cristais - conexão', 'descoberto', 'fazenda vitória - conexão', 'ferreira lage', 'guarará',  'goianá - conexão', 'goiana - conexão', 'joao ferreira - conexão', 'joão ferreira - conexão', 'leopoldina - conexão', 'liberdade - "bassamar"', 'lima duarte', 'mar de espanha', 'maripa de minas - conexão', 'monte verde - conexão', 'olaria', 'orvalho', 'palmital', 'passo pátria', 'passo patria', 'passopatria', 'pedro teixeira', 'pequeri', 'ponte preta - conexão', 'recreio',  'rio novo - conexão', 'rio preto', 'rochedo de minas', 'santa bárbara', 'snt bárbara', 'santa barbara', 'santa helena de minas - conexão', 'santa rita de jacutinga',  'snt rita de jacutinga', 'santana do deserto', 'santo antônio aventureiro', 'santo antonio aventureiro', 'são joão nepomuceno', 'sao joao nepomuceno', 'são roque de minas', 'sao roque de minas', 'são vicente de minas', 'sao vicente de minas', 'senador cortês', 'senador cortes', 'serra bocaina - conexão', 'sossego - conexão', 'tebas - conexão', 'torres', 'três ilhas', 'tres ilhas', '3 ilhas', 'valadares', 'vale sobrado']
#
# VIAÇÃO RIO DOCE:
#
cidade_8 = ['águas pretas', 'aguas pretas', 'almenara', 'araçuaí', 'bicas-trevo', 'guarapari - "rio doce"', 'bicuíba', 'bom jesus do itabapoana', 'cachoeiro de itapemirim', 'camacã', 'camacan', 'campanário', 'campos dos goytacazes', 'campos', 'caratinga', 'carlos chagas', 'dom cavate', 'engenheiro caldas', 'eng caldas', 'eunápolis', 'eunapolis', 'felisburgo', 'frei inocêncio', 'frei inocencio', 'governador valadares', 'ilhéus', 'ilheus', 'inhapim', 'itabacuri', 'itabuna', 'itagimirim', 'itamaraju', 'itambé', 'itaobim', 'itaoca', 'itaperuna',  'jequitinhonha', 'leopoldina - conexão', 'manhuaçu - rio doce', 'marataizes', 'marataízes', 'monte pascoal', 'nanuque', 'novo cruzeiro', 'orizânia', 'pedra azul', 'piúma', 'piuma', 'posto da mata', 'realeza', 'rio do prado', 'santa bárbara do leste', 'santa barbara do leste', 'snt barbara do leste', 'santa clara', 'snt clara', 'teófilo otoni', 'teofilo otoni',  'vargem grande', 'vila velha', 'virgem da lapa', 'vitória', 'vitoria', 'vitória da conquista', 'vitoria da conquista']
#
# VIAÇÃO SANTA CRUZ:
#
cidade_9 = ['aiuruoca', 'alfenas - "santa cruz"', 'americana - "santa cruz"', 'andradas', 'araraquara - "santa"', 'baependi', 'bom jardim de minas', 'bragança paulista - "santa cruz"', 'cambuquira', 'campinas - "santa cruz"', 'carvalhos', 'catanduvas - "sanata cruz"', 'caxambu', 'cruzilia', 'cruzília', 'guaxupé', 'guaxupe', 'lambari', 'passa quatro', 'piracicaba - "santa cruz"', 'pirassununga - "santa cruz"', 'poços de caldas', 'pocos de caldas', 'pouso alegre', 'ribeirão preto', 'ribeirao preto',  'são carlos - "santa cruz"', 'sao carlos - "santa cruz"', 'são josé do rio preto', 'sao jose do rio preto', 'são joão do rio preto - "santa cruz"', 'sao joao do rio preto - "santa cruz"', 'são lourenço', 'sao lourenço', 'sao lourenco', 'são tomé das letras', 'sao tome das letras', 'seritinga', 'três corações', 'tres coraçoes', 'tres coracoes', 'varginha', ]
#
# VIAÇÃO GONTIJO:
#
cidade_10 = ['alto araguaia', 'alto garças', 'anápolis', 'anapolis', 'aracajú - "gontijo"', 'araxá', 'arcos', 'bambuí', 'bom despacho - trevo', 'br estalagem', 'br posto java - trevo', 'campo belo', 'campos altos - trevo', 'cana verde', 'candeias', 'catalão', 'cristais', 'cuiabá', 'divinópolis', 'divinopolis', 'estalagem', 'feira de santana', 'formiga', 'goiânia - gontijo', 'goiania - gontijo', 'iguatama', 'itumbiara', 'jaciara', 'jataí', 'jequié', 'joão pessoa', 'joao pessoa', 'luz - trevo', 'mineiros', 'nova ponte - trevo', 'nova serrana - gontijo', 'oliveira', 'perdões', 'perdoes', 'posto java - trevo', 'rio verde', 'rondonópolis', 'rondonopolis', 'santa juliana - trevo', 'snt juliana', 'uberaba', 'uberlândia - gontijo', 'porto velho - conexão']
#
# VIAÇÃO PARAIBUNA:
#
cidade_11 = ['alto jequitibá', 'alvorada de minas', 'argirita', 'bom jesus da cachoeira', 'caparaó divino', 'carangola', 'cataguases', 'conceição do monte alegre - "paraibuna"', 'espera feliz', 'fervedouro', 'fortaleza de minas', 'guarará', 'laranjal', 'leopoldina', 'liberdade', 'manhuaçu', 'manhumirim', 'maripá de minas', 'matias barbosa - "paraibuna"', 'mindurí', 'miguel pereira - "paraibuna"', 'miradouro', 'miraí', 'monte verde', 'muriaé', 'parque nacional caparaó', 'passo da pátria', 'ponte preta', 'santa helena de minas', 'serra bocaina', 'simão pereira', 'sossego', 'tebas']
#
# VIAÇÃO UNIÃO:
#
cidade_12 = ['alto paraíso de goiás', 'araguari', 'arraias', 'belém', 'bocaiúva', 'buenópolis', 'caldas novas', 'campos belos', 'conceição do tocantins', 'corinto', 'curvelo', 'goiânia - expresso união', 'goiania - expresso união', 'janaúba', 'jaraguá', 'jaragua', 'lages', 'mafra', 'maringá', 'medina', 'monte alegre de goiás', 'monte carmelo', 'montes claros', 'natividade', 'nova serrana - união', 'palmas', 'paracatu','paracatú', 'patos de minas', 'patrocínio', 'piracanjuba', 'pirapora', 'planaltina', 'porangatu', 'porto nacional', 'rialma', 'santa rosa do tocantins', 'santo ângelo', 'são gabriel', 'são joão daliança', 'são joão da aliança', 'sao joao da aliança', 'são luiz gonzaga', 'sete lagoas', 'silvanópolis', 'três marias', '3 marias', 'tres marias',  'unaí', 'uruaçú', 'uberlândia - união']
#
# VIAÇÃO UNICA:
#
cidade_13 = ['areal', 'búzios - conexão', 'buzios - conexão', 'cabo frio - unica facil', 'itaipava', 'nova friburgo', 'nova iguaçú', 'petrópolis - viação unica', 'petropolis - viação unica', 'rio bonito', 'são pedro da aldeia - unica facil', 'sao pedro da aldeia - unica facil']
#
# VIAÇÃO JOSÉ MARIA RODRIGUES:
#
cidade_14 = ['aeroporto - "jmr"', 'astolfo dutra', 'campestre', 'coronel pacheco', 'dona euzébia', 'dona euzebia', 'goianá', 'goiana', 'guarani', 'guaraní', 'joão ferreira', 'joao ferreira', 'piau', 'piraúba', 'pirauba', 'rio novo', 'sobral pinto', 'toledos', 'triqueda']
#
# VIAÇÃO ÀGUIA BRANCA:
#
cidade_15 = ['foz do iguaçú', 'foz do iguaçu', 'foz do iguacu', 'são josé dos campos - aguia branca', 'sao jose dos campos - aguia branca', 'taubaté - "aguia branca"', 'são paulo - "aguia branca"', 'sao paulo - "tietê"', 'são paulo - "tietê"', 'sao bernardo do campo - "aguia branca"', 'são bernardo do campo - "aguia branca"',]
#
# VIAÇÃO ITAPEMIRIM:
#
cidade_16 = ['aracajú - "itapemirim"', 'belo horizonte - "itapemirim"', 'campina grande', 'curitiba - "itapemirim"', 'feira de santana - "itapemirim"', 'guarapari - "itapemirim"', 'ipatinga - "itapemirim"', 'nanuque - itapemirim', 'rio de janeiro - itapemirim' , 'salvador', 'são paulo - itapemirim', 'sao paulo - itapemirim', 'vitória da conquista - itapemirim', 'vitoria da conquista - ']
#
# VIAÇÃO brasil bus:
#
cidade_17 = ['petrópolis - "brasil bus"', 'petropolis - "brasil bus"', 'magé', 'são pedro da aldeia - "brasil bus"', 'sao pedro da aldeia - "brasil bus"', 'cabo frio - "brasil bus"']
#
# VIAÇÃO RODE ROTAS:
#
cidade_18 = ['uruaçú - rode rotas', 'porangatú - rode rotas', 'gurupí - "rota rotas"', 'paraíso do tocantins', 'miranorte', 'guaraí', 'araguaína', 'estreito', 'porto franco', 'imperatriz - rode rotas', 'açailândia', 'itinga do maranhão', 'dom eliseu', 'ulianópolis', 'ulianopolis', 'paragominas', 'ipixuna', 'mãe do rio', 'são miguel do guama', 'santa maria do pará', 'castanhal', 'ananindeua', 'belém - "rode rotas"']
#
#
# LISTA DE CIDADES POR TARIFAS:
#
# Referente ao valor da tarifa de R$0,85
#
tarifa_1 = ['aeroporto - "bassamar"', 'aeroporto - "jmr"', 'goianá', 'goiana', 'goianá - conexão', 'goiana - conexão', 'conceição do rio verde', 'conceicao do rio verde', 'conceiçao do rio verde', 'coronel pacheco', 'coronel pacheco - conexão', 'ewbank da câmara', 'ewbank da camara', 'ewbank', 'eubank da camara', 'ferreira lage', 'joão ferreira', 'joao ferreira', 'joao ferreira - conexão', 'joão ferreira - conexão', 'matias barbosa', 'matias barbosa - "paraibuna"', 'monte verde', 'monte verde - conexão', 'passo da pátria', 'passo da patria', 'santa bárbara', 'snt bárbara', 'santa barbara', 'são roque de minas', 'sao roque de minas', 'senador cortês', 'senador cortes', 'triqueda', 'valadares'] 
#
# Referente ao valor da tarifa de R$1,45
#
tarifa_2 = ['afonso arinos', 'bela vista de minas', 'bias fortes', 'bicas', 'bicas-conexão', 'boa vista', 'bom jardim de minas', 'bom jardim de minas - conexão', 'br 267 - guarará', 'cachoeira', 'caranguejo', 'chiador', 'conceiçao', 'conceicao', 'conceição', 'correia de almeida', 'cristais - conexão', 'faixa azul', 'fazenda vitória - conexão', 'guarani', 'guaraní', 'guarará', 'guarara', '*guarará', '*guarara', 'lima duarte', 'mar de espanha', 'maripá de minas - conexão', 'maripa de minas - conexão', 'olaria', 'orvalho', 'palmital','paraíba do sul', 'paraiba do sul', 'passo pátria', 'passo patria', 'passopatria', 'pedro teixeira', 'pequeri', 'pequerí', 'peróbas', 'perobas', 'piau', 'ponte preta', 'ponte preta - conexão', 'rio novo', 'rio novo - conexão', 'rio pomba', 'rochedo de minas', 'santa helena de minas', 'santa helena de minas - conexão', 'snt helena de minas',  'santo antônio aventureiro', 'santos dumont', 'são joão da serra', 'sao joao da serra', 'são joão nepomuceno', 'sao joao nepomuceno', 'simão pereira', 'simao pereira', 'sossego', 'sossego - conexão', 'tabuleiro']
#
# Referente ao valor da tarifa de R$2,55
#
tarifa_3 = ['além paraíba', 'alem paraiba', 'além paraiba', 'alem paraíba', 'acampamento de campelina', 'alto jequitibá', 'alto jequitiba', 'alvorada de minas', 'argirita', 'argirita - conexão', 'astolfo dutra', 'barbacena', 'barroso', 'bom jesus da cachoeira', 'caieiro', 'campestre', 'carandaí', 'carandai', 'coimbra', 'ubá', 'uba', 'visconde do rio branco', 'cataguases', 'conceição do monte alegre - "bassamar"', 'conceição do monte alegre - "paraibuna"', 'conservatória', 'conservatoria', 'descoberto', 'dona euzébia', 'dores de campos', 'ervália', 'ervalia', 'fortaleza de minas', 'helvas', 'ibertioga', 'itaipava', 'laranjal', 'levy gasparian', 'madre de deus', 'manoel duarte', 'mercês', 'merces', 'minduri', 'mindurí', 'miguel pereira', 'miguel pereira - "paraibuna"', 'nova friburgo', 'nova iguaçú', 'nova iguaçu', 'paraíba do sul', 'paraiba do sul', 'petrópolis - viação unica', 'petropolis - viação unica', 'petrópolis - "brasil bus"', 'petropolis - "brasil bus"', 'pirapitinga', 'piraúba', 'pirauba', 'prados', 'ressaquinha', 'rio das flores', 'rio preto', 'santana do deserto', 'são pedro da aldeia - unica facil', 'sao pedro da aldeia - unica facil', 'são pedro da aldeia - "brasil bus"', 'sao pedro da aldeia - "brasil bus"', 'são sebastião da vitória', 'sao sebastiao da vitoria', 'senador firmino', 'serra bocaina', 'serra bocaina - conexão', 'sobral pinto', 'tebas - conexão', 'tebas', 'tiradentes', 'tocantins', 'toledos', 'três ilhas', 'tres ilhas', '3 ilhas', 'três rios',  'tres rios', '3 rios', 'vale sobrado', 'valença', 'vassouras', 'visconde do rio branco'] 
#
# Referente ao valor da tarifa de R$5,25
#
tarifa_4 = ['alegrete', 'aiuruoca', 'almenara', 'alfenas - "cometa"', 'alfenas - "santa cruz"', 'alto araguaia', 'alto garças', 'alto garcas', 'águas pretas', 'aguas pretas', 'águas de lindóia', 'aguas de lindoia', 'alto paraíso de goiás', 'alto paraiso de goias', 'americana', 'americana - "santa cruz"', 'anápolis', 'andradas', 'andrelândia', 'angra dos reis', 'aparecida do norte', 'aracajú - "itapemirim"', 'aracajú - "gontijo"', 'araçuaí', 'araguari', 'arantina', 'araraquara', 'araraquara - "santa cruz"', 'araxá', 'arcos', 'areal', 'arraias', 'baependi', 'bambuí', 'bananal', 'barra do piraí', 'barra mansa', 'belém', 'belo horizonte', 'belo horizonte - "itapemirim"', 'betim', 'bicas-trevo', 'bicuíba', 'bicuiba', 'bocaiúva', 'bocaiuva', 'bom despacho - trevo', 'bom jesus do itabapoana', 'bragança paulista', 'bragança paulista - "santa cruz"', 'brasília', 'buenópolis', 'buenopolis', 'búzios - conexão', 'buzios - conexão', 'cabo frio - unica facil', 'cabo frio - "brasil bus"', 'cachoeiro de itapemirim', 'caldas novas', 'camacã', 'camacan', 'cambuquira', 'campanario', 'campanário', 'campinas', 'campinas - "santa cruz"', 'campina grande', 'campo belo', 'campos dos goytacazes', 'cdg', 'campos goytacazes', 'campos altos - trevo', 'campos belos', 'campo mourão', 'campo mourao', 'cana verde', 'candeias', 'caparaó divino', 'caparao divino', 'carangola', 'caratinga', 'carlos chagas', 'carvalhos', 'catalao', 'catalão', 'catanduvas - "santa cruz"', 'catanduvas', 'caxambu', 'caxias', 'conceição do tocantins', 'conceicao do tocantins','cdt', 'congonhas', 'conselheiro lafayete', 'contagem', 'corinto', 'coronel fabriciano', 'cruzilia', 'cruzília',  'cuiabá', 'cuiaba', 'curitiba', 'curitiba - "itapemirim"', 'curvelo', 'divinópolis', 'divinopolis', 'dom cavate', 'engenheiro caldas', 'eng caldas', 'espera feliz', 'estalagem', 'eunápolis', 'eunapolis', 'extrema', 'cristais', 'feira de santana', 'feira de santana - "itapemirim"', 'felisburgo', 'fervedouro', 'florianópolis', 'florianopolis', 'formiga', 'foz do iguaçu', 'foz do iguaçú', 'foz do iguacu', 'frei inocêncio', 'frei inocencio', 'goiânia - "expresso união"', 'goiania - "expresso união"', 'goiânia - "util"', 'goiania - "util"', 'goiânia - "gontijo"', 'goiania - "gontijo"', 'governador valadares', 'guarapari - "itapemirim"',  'guaxupé', 'iguatama', 'ilhéus', 'ipatinga', 'ipatinga - "itapemirim"', 'imperatriz', 'inhapim', 'itabacuri', 'itabacurí', 'itabira', 'itabuna', 'itagimirim', 'itamaraju', 'itambé', 'itaobim', 'itaoca', 'itaperuna', 'itaúna', 'itauna', 'itumbiara', 'itutinga', 'jacareí', 'jacarei', 'jaciara', 'janaúba', 'janauba', 'jaraguá', 'jaragua', 'jataí', 'jequié',  'jequitinhonha', 'joão molevade', 'joao molevade', 'joão pessoa', 'joao pessoa', 'joinvile', 'jundiaí', 'jundiai', 'lages', 'lambarí', 'lavras', 'leopoldina', 'leopoldina - conexão', 'leopoldina - conexão_2','liberdade', 'liberdade - "bassamar"', 'londrina', 'macaé', 'macae', 'madureira', 'mafra', 'manhuaçu - rio doce', 'manhuaçu', 'manhumirim', 'marataizes', 'mariana', 'maringá', 'medianeira', 'medina', 'mineiros', 'miracema', 'miradouro', 'miraí', 'mirai', 'mogi mirim', 'mogi das cruzes', 'mogi guaçu', 'mogi guaçú', 'monte alegre de goiás', 'monte alegre de goias', 'monte carmelo', 'monte pascoal', 'montes claros', 'muriaé', 'nanuque', 'nanuque - itapemirim', 'natal', 'natividade', 'niterói', 'niteroi', 'nova era', 'nova ponte - trevo', 'nova serrana - gontijo', 'nova serrana - união', 'novo cruzeiro', 'oliveira', 'ourinhos', 'ouro branco', 'ouro preto', 'orizânia', 'orizania', 'palmas', 'paracatu' 'paracatú', 'pará de minas', 'pará de minas', 'parati', 'parque nacional caparaó', 'parque nacional caparao', 'passa quatro', 'passa 4', 'patos de minas', 'patrocínio', 'patrocinio', 'pedra azul', 'perdões', 'perdoes', 'pernambuco', 'piracanjuba', 'piracicaba - "santa cruz"', 'piracicaba', 'pirapora', 'pirassununga', 'pirassununga - "santa cruz"', 'piúma', 'piuma', 'planaltina', 'poços de caldas', 'ponte nova', 'porangatu', 'porangatú', 'porto alegre',  'porto firme', 'porto nacional', 'posto da mata', 'pouso alegre', 'raposo', 'realeza', 'recreio', 'resende', 'rialma', 'ribeirão preto', 'ribeirão preto - "cometa"','ribeirao preto - "cometa"', 'rio bonito', 'rio casca', 'rio das ostras - próximo secretaria de turismo', 'rio de janeiro', 'rio de janeiro - conexão', 'rio do prado', 'rio verde', 'rondonópolis', 'rondonopolis', 'santa bárbara do leste', 'santa clara', 'snt clara', 'santa juliana - trevo', 'snt juliana', 'santa rita de jacutinga', 'snt rita de jacutinga', 'santa rosa do tocantins', 'santo andré', 'santo andre', 'santo ângelo', 'santo angelo', 'santos', 'são bernardo do campo', 'sao bernardo do campo', 'sao bernardo do campo - "aguia branca"', 'são bernardo do campo - "aguia branca"', 'são caetano', 'sao caetano', 'são carlos', 'são carlos - "santa cruz"', 'são domingos do prata', 'são gabriel', 'são geraldo', 'são gonçalo do sapucaia', 'são joão daliança', 'são joão del rei', 'são josé do rio preto', 'são joão do rio preto', 'são joão do rio preto - "santa cruz"' 'são josé dos campos', 'são lourenço', 'são luiz gonzaga', 'são paulo', 'sao paulo', 'são paulo - "itapemirim"', 'sao paulo - "itapemirim"', 'são tomé das letras', 'sao tome das letras', 'são vicente de minas', 'sao vicente de minas', 'seritinga', 'serraria', 'sete lagoas', 'silvanópolis', 'silvanopolis', 'sorocaba', 'taubaté', 'taubaté - "aguia branca"', 'teixeiras', 'teófilo otoni', 'teofilo otoni', 'timóteo', 'timoteo', 'torres', 'três corações', 'tres coraçoes', '3 coracoes', 'três marias', 'tres marias', '3 marias', 'uberaba', 'uberlândia - gontijo', 'uberlândia - união', 'unaí', 'unai', 'uruaçu', 'uruaçú', 'vargem grande', 'varginha', 'viçosa', 'vicosa', 'vila velha', 'virgem da lapa', 'vitória', 'vitória da conquista', 'vitoria da conquista', 'vitória da conquista - itapemirim', 'vitoria da conquista - itapemirim', 'volta redonda', 'br estalagem', 'br posto java - trevo', 'porto velho - conexão', 'luz - trevo', 'posto java - trevo', 'magé', 'são josé dos campos - "util"', 'sao jose dos campos - "util"', 'são josé dos campos - "aguia branca"', 'sao jose dos campos - "aguia branca"', 'são paulo - "aguia branca"', 'sao paulo - "tietê"', 'são paulo - "tietê"', 'são paulo - "cometa"', 'sao paulo - "cometa"', 'uruaçú - "rode rotas"', 'porangatú - "rode rotas"', 'gurupí - "rota rotas"', 'paraíso do tocantins', 'miranorte', 'guaraí', 'araguaína', 'estreito', 'porto franco', 'imperatriz - "rode rotas"', 'açailândia', 'itinga do maranhão', 'dom eliseu', 'ulianópolis', 'ulianopolis', 'paragominas', 'ipixuna', 'gurupí - "util"', 'mãe do rio', 'são miguel do guama', 'santa maria do pará', 'castanhal', 'ananindeua', 'belém - "rode rotas"', 'sao joao do rio preto - "santa cruz"', 'sao joao do rio preto', 'guarapari - "rio doce"']
#
#LISTA_GERAL:
#
lista_geral = ['inss', 'previdencia', 'previdência', 'previdência social', 'conselho tutelar',  'juizado de menores' , 'juizado menores', 'smu', 'antt', 'guarda municipal', 'gm', 'cargas util', 'util cargas', 'encomendas ceu', 'ceu encomendas', 'ceu', 'andré', 'andre', 'André', 'Andre', 'cargas resendense', 'resendense cargas', 'resendense', 'edimar despachante', 'despachante',  'migração', 'centro pop', 'centropop', 'balcão', 'balcao' , 'amd', 'amd balcão', 'rodoviaria', 'rodoviária', 'amd services', 'adm', 'secrretaria', 'diretoria', 'mensalista', 'estacionamento', 'estacionamento pago', 'estacionamento mensalista', 'rei do mate', 'rm', 'cacaushow', 'cs', 'cacau', 'chocolateria', 'emporio rural', 'empório rural', 'emporio', 'empório', 'rural', 'bomboniere', 'vitoria', 'vitória', 'bombonier', 'pastelaria', 'princesa dos pastéis', 'côrrea', 'lanchonete', 'santa lúcia', 'lanchonete santa lúcia', 'santalucia', 'snt lucia', 'farmácia', 'farmacia', 'poderosa', 'poderosa presentes', 'poderosa loja', 'poderosapresentes', 'belinha', 'eletrônicos', 'belinha eletrônicos', 'eletronicos', 'padaria', 'estação mineira', 'estacao mineira', 'box100', 'box 100', 'box', 'center tour', 'centertour', 'centertur', 'center tur', 'p1', 'p01', 'p 1', 'p 01', 'p2', 'p02', 'p 2', 'p 02', 'p3', 'p03', 'p 3', 'p 03', 'p4', 'p04', 'p 4', 'p 04', 'p5', 'p05', 'p 5', 'p 05', 'p6', 'p06', 'p 6', 'p 06', 'p7', 'p07', 'p 7', 'p 07','p8', 'p08', 'p 8', 'p 08', 'p9', 'p09', 'p 9', 'p 09', 'p1', 'p01', 'p 1', 'alfa1', 'alfa 01', 'alfa1', 'alpha1', 'alpha 1', 'alfa2', 'alfa 02', 'alfa2', 'alpha2', 'alpha 2', 'alfa3', 'alfa 03', 'alfa3', 'alpha3', 'alpha 3', 'alfa4', 'alfa 04', 'alfa4', 'alpha4', 'alpha 4', 'alfa5', 'alfa 05', 'alfa5', 'alpha5', 'alpha 5', 'alfa1', 'alfa 06', 'alfa6', 'alpha6', 'alpha 6', 'alfa7', 'alfa 7', 'alfa7', 'alpha7', 'alpha 7', 'alfa8', 'alfa 08', 'alfa8', 'alpha8', 'alpha 8', 'alfa9', 'alfa 09', 'alfa9', 'alpha9', 'alpha 9', 'alfa10', 'alfa 10', 'alfa10', 'alpha10', 'alpha 10', 'alfa11', 'alfa 11', 'alfa11', 'alpha11', 'alpha 11', 'saritur', 'coordenadas', 'atual', 'util', 'brisa', 'guanabara', 'sampaio', 'gypsyy', 'cometa', 'catarinense', 'expresso do sul', 'expressodosul', '1001', 'progresso', 'viaçãoprogresso', 'viacao progresso', 'viaçao progresso', 'unida', 'viação unida', 'viaçãounida', 'unidamansur', 'unida manssur', 'transur', 'viação transur', 'bassamar', 'viacao bassamar', 'riodoce', 'rio doce', 'viação rio doce', 'santa cruz', 'snt cruz', 'sntcruz', 'santacruz', 'sulminas', 'sul minas', 'gontijo', 'viação gontijo', 'viacao gontijo', 'paraibuna', 'viação paraibuna', 'viação união', 'união', 'uniao', 'expresso união', 'pluma', 'viação pluma', 'viação unica', 'unica', 'unica fácil', 'unica facil', 'unicafacil', 'josé maria rodrigues', 'jmr', 'jose maria rodrigues', 'josemariarodrigues', 'águiabranca', 'águia branca', 'aguia branca', 'águiabranca', 'roderotas', 'rode rotas', 'itapemirim', 'viação itapemirim', 'kaissara', 'viação kaissara', 'brasilbus', '"brasil bus"', 'guarapari - "rio doce"']
#
#
#
class MainApp(App):
    def build(self):
        self.combined_cidades = self.get_combined_cidades()
        self.title = "AMD BUSCA - v1.0.6_2025_03_31 | Desenvolvido por: Fabiano Landim"
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Layout horizontal para o título e a imagem
        header_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)
        
        # Título principal com design moderno
        title = Label(
            text="[b][color=#1E90FF]AMD BUSCA[/color][/b]",
            font_size=32,
            markup=True,
            halign='center',
            valign='middle'
        )
        title.bind(size=title.setter('text_size'))
        
        # Adicionando o título e a imagem ao layout horizontal
        header_layout.add_widget(title)
        
        # Adicionando o cabeçalho ao layout principal
        layout.add_widget(header_layout)
        
        # Subtítulo ou descrição abaixo do título
        subtitle = Label(
            text="Busque resultados com precisão e eficiência.",
            font_size=14,
            size_hint_y=None,
            height=30,
            color=(0.5, 0.5, 0.5, 1),  # Cinza claro para um tom profissional
            halign='center'
        )
        layout.add_widget(subtitle)
        
        # Campo de entrada com estilo moderno
        self.input = TextInput(
            hint_text="Digite o nome da cidade ou termo de pesquisa...",
            font_size=16,
            size_hint_y=None,
            height=30,
            background_color=(0.95, 0.95, 0.95, 1),  # Fundo claro para o campo de entrada
            foreground_color=(0.2, 0.2, 0.2, 1),     # Texto escuro para contraste
            multiline=False
        )
        self.input.bind(text=self.update_suggestions)
        layout.add_widget(self.input)
        
        # Layout para botões com design moderno
        button_layout = BoxLayout(size_hint_y=None, height=60, spacing=15)
        
        search_button = Button(
            text="Pesquisar",
            on_press=self.pesquisar,
            background_color=(0.1, 0.5, 0.9, 1),  # Azul vibrante para chamar atenção
            color=(1, 1, 1, 1),                   # Texto branco para contraste
            font_size=16
        )
        clear_button = Button(
            text="Limpar",
            on_press=self.limpar,
            background_color=(0.8, 0.2, 0.2, 1),  # Vermelho suave para ação de limpeza
            color=(1, 1, 1, 1),
            font_size=16
        )
        exit_button = Button(
            text="Sair",
            on_press=self.sair,
            background_color=(0.3, 0.3, 0.3, 1),  # Cinza escuro para sair
            color=(1, 1, 1, 1),
            font_size=16
        )
        button_layout.add_widget(search_button)
        button_layout.add_widget(clear_button)
        button_layout.add_widget(exit_button)
        layout.add_widget(button_layout)
        
        # Área de sugestões com scroll (reduzida para liberar espaço)
        self.suggestions_grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.suggestions_grid.bind(minimum_height=self.suggestions_grid.setter('height'))
        scroll_suggestions = ScrollView(size_hint=(1, None), height=100)  # Altura reduzida
        scroll_suggestions.add_widget(self.suggestions_grid)
        layout.add_widget(scroll_suggestions)
        
        # Área de saída com scroll (otimizada para maior visibilidade)
        scroll_view = ScrollView(size_hint_y=0.6)  # Aumenta a proporção vertical
        self.output = Label(
            text="",
            font_size=15,
            size_hint_y=None,
            text_size=(None, None),  # Permite que o texto se ajuste automaticamente
            markup=True,
            color=(0.9, 0.9, 0.9, 0.9),  # Texto escuro para legibilidade
            padding=(10, 10),  # Adiciona espaçamento interno para melhorar a aparência
            halign='left',
            valign='top'
        )
        self.output.bind(size=self.adjust_output_height)
        scroll_view.add_widget(self.output)
        layout.add_widget(scroll_view)
        
        return layout

    def adjust_output_height(self, instance, value):
        self.output.height = max(instance.texture_size[1], 400)
    #
    def get_combined_cidades(self):
        return (
            cidade_1 + cidade_2 + cidade_3 + cidade_4 + cidade_5 + cidade_6 + cidade_7 +
            cidade_9 + cidade_10 + cidade_11 + cidade_12 + cidade_13 + cidade_14 + cidade_15 + cidade_16 + cidade_17 + cidade_18 + lista_geral
        )
    def update_suggestions(self, instance, value):
        self.suggestions_grid.clear_widgets()
        input_text = value.lower()
        if not input_text:
            return
        
        matches = [cidade for cidade in self.combined_cidades if input_text in cidade]
        seen = set()
        unique_matches = []
        for match in matches:
            if match not in seen:
                seen.add(match)
                unique_matches.append(match)
        
        for match in unique_matches[:5]:
            btn = Button(text=match, size_hint_y=None, height=40, background_color=('#5F9EA0'))
            btn.bind(on_release=lambda b: self.select_suggestion(b.text))
            self.suggestions_grid.add_widget(btn)
    def select_suggestion(self, text):
        self.input.text = text
        self.suggestions_grid.clear_widgets()
        self.pesquisar(None)
    #
    #
    def pesquisar(self, instance):
        nome  = self.input.text.lower()
        resultado = "-=-=-=-=-=-=-= DESCONHECIDO -=-=-=-=-=-=-=-=-\n\n> CONFIRA O NOME PESQUISADO, E TENTE NOVAMENTE!\n> POSSIBILIDADE DE NÃO CONSTAR NESSE BANCO DE DADOS!\n> CLIQUE EM LIMPAR PARA UMA NOVA PESQUISA!"
        #
        #
        # COORDENADAS / ATUAL:
        #
        if nome in cidade_1 and nome  in tarifa_3:
            resultado = (
                '=-=-=- EMPRESA: VIAÇÃO COORDENADAS - ATUAL =-=-=-\n\n'
                'CONTATO: (32) 3112-0423 - GUICHÊS: 04 e 05\n'
                'SITE: https://www.saritur.com.br/\n'
                'FUNCIONAMENTO: dom a sex das 06h30 - 00h45\n'
                'sab de 06h30 - 19h10\n'
                'PLATAFORMA: 22\n\n'
				'TARIFA DE EMBARQUE R$2,55'
            )
        #
        #
        # COORDENADAS / ATUAL:
        #
        elif nome  in cidade_1 and nome  in tarifa_4:
            resultado = (
                '=-=-=- EMPRESA: VIAÇÃO COORDENADAS - ATUAL =-=-=-\n\n'
                'CONTATO: (32) 3112-0423 - GUICHÊS: 04 e 05\n'
                'SITE: https://www.saritur.com.br/\n'
                'FUNCIONAMENTO: dom a sex das 06h30 - 00h45\n'
                'sab de 06h30 - 19h10\n'
                'PLATAFORMA: 22\n\n'
				'TARIFA DE EMBARQUE R$5,25'
            )
        #
        #
        # UTIL / BRISA / SAMPAIO / GUANABARA / REAL EXPRESSO / RÀPIDO FERDERAL / GYPSYY:
        #
        elif nome  in cidade_2 and nome  in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY\nGUANABARA / REAL EXPRESSO / RÁPIDO FEDERAL\n\n'
               'GUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830 - WHATSAPP:(32)98833-5497\n\nSITE:\n' 
				'UTIL: https://www.util.com.br/\nGUANABARA: https://www.viajeguanabara.com.br/\nSAMPAIO: https://viacaosampaio.com.br/\n\nPLATAFORMAS: 13, 14, e 15\n\n'
                'TARIFA DE EMBARQUE R$2,55'
            )
        #
        #
        # UTIL / BRISA / SAMPAIO / GUANABARA / REAL EXPRESSO / RÀPIDO FERDERAL / GYPSYY:
        #
        elif nome  in cidade_2 and nome  in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY\nGUANABARA / REAL EXPRESSO / RÁPIDO FEDERAL\n\n'
               'GUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830 - WHATSAPP:(32)98833-5497\n\nSITE:\n' 
				'UTIL: https://www.util.com.br/\nGUANABARA: https://www.viajeguanabara.com.br/\nSAMPAIO: https://viacaosampaio.com.br/\n\nPLATAFORMAS: 13, 14, e 15\n\n'
                'TARIFA DE EMBARQUE R$5,25'
            )
        #
        #
        # VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001:
        #
        elif nome  in cidade_3 and nome  in tarifa_4:
            resultado = (
				'-=-=-= EMPRESA: VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001 -=-=-=\n\n' 
                'GUICHÊS 15 e 16 - CONTATO: 4004-9600 e 0800 942 0030\n\nSITE:\n' 
                'COMETA: https://www.cometa.com.br\nCATARINENSE: https://www.catarinense.com.br\n' 
                'EXPRESSO DO SUL: https://www.expressodosul.com.br\nVIAÇÃO1001: https://www.autoviacao1001.com.br\n' 
                'FUNCIONAMENTO: DIARIAMENTE 07h30 - 11h - 12h - 23h30\n' 
                'PLATAFORMAS: 10, 11 e 12\n\n'
			    'TARIFA DE EMBARQUE R$5,25'
		    )
        #
        #
        # VIAÇÃO PROGRESSO:
        #
        elif nome  in cidade_4 and nome  in tarifa_1:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
                'CONTATOS:\n\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\nCENTER TOUR: (32) 3025-3936\n' 
                'SITE: https://www.viacaoprogresso.com.br\nFUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\n' 
                'PLATAFORMAS: 25 e 26\n\n' 
                'TARIFA DE EMBARQUE R$0,85'
			)
        #
        #
        # VIAÇÃO PROGRESSO:
        #
        elif nome  in cidade_4 and nome  in tarifa_2:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
                'CONTATOS:\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\n' 
                'CENTER TOUR: (32) 3025-3936\nSITE: https://www.viacaoprogresso.com.br\n' 
                'FUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\nPLATAFORMAS: 25 e 26\n\n'
                'TARIFA DE EMBARQUE R$1,45'
			)
        #
        #
        # VIAÇÃO PROGRESSO:
        #
        elif nome  in cidade_4 and nome  in tarifa_3:
            resultado= (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
				'CONTATOS:\n'
				'RODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\n' 
				'CENTER TOUR: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\n' 
				'PLATAFORMAS: 25 e 26\n\n' 
				'TARIFA DE EMBARQUE R$2,55'
			)
        #
        #
        # VIAÇÃO PROGRESSO:
        #
        elif nome  in cidade_4 and nome  in tarifa_4:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
				'CONTATOS:\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\n' 
				'CENTER TOUR: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\n' 
				'PLATAFORMAS: 25 e 26\n\n' 
				'TARIFA DE EMBARQUE R$5,25'
			)
		#
        #
        # VIAÇÃO UNIDA:
        #
        elif nome  in cidade_5 and nome  in tarifa_1:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n' 
                'CONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n'  
                'FUNCIONAMENTO:\nseg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
                'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$0,85'
			)
        #
        #
        # VIAÇÃO UNIDA:
        #
        elif nome  in cidade_5 and nome  in tarifa_2:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n' 
                'CONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n' 
                'FUNCIONAMENTO:\nseg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
				'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$1,45'
            )
        #
        #
        # VIAÇÃO UNIDA:
        #
        elif nome  in cidade_5 and nome  in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n' 
				'SITE: https://unidamansur.queropassagem.com.br\n' 
				'FUNCIONAMENTO:\nseg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
				'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$2,55'
			)
		#
        #
        # VIAÇÃO UNIDA:
        #
        elif nome  in cidade_5 and nome  in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n' 
                'CONTATO: (32) 3215-3427\nSITE: https://unidamansur.queropassagem.com.br\n' 
                'FUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
                'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        # VIAÇÃO TRANSUR:
        #
        elif nome  in cidade_6 and nome  in tarifa_2:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10=-=-=-\n\nCONTATO: (32) 3218-3613\n' 
                'SITE: https://https://www.transur.com.br/horarios_preco\n' 
                'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h\n' 
                'ter à  dom: 06h30- 12h - 13h -19h\n' 
                'PLATAFORMA: 17\n\n' 
                'TARIFA DE EMBARQUE R$1,45'
			)
        #
        #
        # VIAÇÃO TRANSUR:
        #
        elif nome  in cidade_6 and nome  in tarifa_3:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10=-=-=-\n\nCONTATO: (32) 3218-3613\n' 
                'SITE: https://https://www.transur.com.br/horarios_preco\n' 
                'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h - ter à  dom: 06h30- 12h - 13h -19h\n' 
                'PLATAFORMA: 17\n\n' 
                'TARIFA DE EMBARQUE R$2,55'
			)
        #
        #
        # VIAÇÃO TRANSUR:
        #
        elif nome  in cidade_6 and nome  in tarifa_4:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10=-=-=-\n\nCONTATO: (32) 3218-3613\n' 
                'SITE: https://https://www.transur.com.br/horarios_preco\n' 
                'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h\n		ter à  dom: 06h30- 12h - 13h -19h\n' 
                'PLATAFORMA: 17\n\n'
                'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        # VIAÇÃO BASSAMAR:
        #
        elif nome  in cidade_7 and nome  in tarifa_1:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
                'SITE: https://www.viacaobassamar.queropassagem.com.br\n' 
                'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$0,85'
			)
        #
        #
        # VIAÇÃO BASSAMAR:
        #
        elif nome in cidade_7 and nome in tarifa_2:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
                'SITE: https://www.viacaobassamar.queropassagem.com.br\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$1,45'
			)
        #
        #
        # VIAÇÃO BASSAMAR:
        #
        elif nome in cidade_7 and nome in tarifa_3:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
				'SITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$2,55'
			)
		#
        #
        # VIAÇÃO BASSAMAR:
        #
        elif nome in cidade_7 and nome in tarifa_4:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
				'SITE: https://www.viacaobassamar.queropassagem.com.br\n'
				'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        # VIAÇÃO RIO DOCE:
        #
        elif nome in cidade_8 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\n' 
				'SITE: http://www.viacaoriodoce.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 07h - 21h\n'
				'PLATAFORMA: 24\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)

        elif nome == 'guarapari - "rio doce"':
            resultado = (
				'EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\n' 
				'SITE: http://www.viacaoriodoce.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 07h - 21h\n'
				'PLATAFORMA: 24\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
		#
        #
        # VIAÇÃO SANTA CRUZ:
        #
        elif nome in cidade_9 and nome in tarifa_2:
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\n' 
				'SITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMA: 16\n\n'
				'TARIFA DE EMBARQUE R$1,45'
			)
        #
        #
        # VIAÇÃO SANTA CRUZ:
        #
        elif nome in cidade_9 and nome in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\n' 
				'SITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n'
				'PLATAFORMA: 16\n\n'
				'TARIFA DE EMBARQUE R$2,55'
			)
		#
        #
        # VIAÇÃO SANTA CRUZ:
        #
        elif nome in cidade_9 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\n' 
				'SITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMA: 16\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        # VIAÇÃO GONTIJO:
        #
        elif nome in cidade_10 and nome in tarifa_4:
            resultado = (
				'EMPRESA:VIAÇÃO GONTIJO - GUICHÊ: 27\n\nCONTATO:(32) 3215-9458  -  (32) 98710-6414\n' 
				'SITE: https://www.gontijo.com.br/\n\nFUNCIONAMENTO: seg- sex 08h - 20h\nsab - dom - feriados 08h - 12h / 14h - 17h20\n' 
				'PLATAFORMA: 27\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        # VIAÇÃO SANTA PARAIBUNA:
        #
        elif nome in cidade_11 and nome in tarifa_1:
            resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n'
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO: seg à qui: 05h45 - 10h30 - 11h30 às 18h\nsex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n'
				'PLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$0,85'
			)
		#
        #
        # VIAÇÃO SANTA PARAIBUNA:
        #
        elif nome in cidade_11 and nome in tarifa_2:
           	resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n'
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO:\n\nseg à qui: 05h45 - 10h30 - 11h30 às 18h\nsex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n' 
				'PLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$1,45'
			)
        #
        #
        # VIAÇÃO SANTA PARAIBUNA:
        #
        elif nome in cidade_11 and nome in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n' 
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO:\n\neg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n' 'PLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$2,55'
			)
		#
        #
        # VIAÇÃO SANTA PARAIBUNA:
        #
        elif nome in cidade_11 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n'
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO:\n\nseg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        #  VIAÇÃO EXPRESSO UNIÃO / PLUMA:
        #
        elif nome in cidade_12 and nome in tarifa_4:
           resultado = (
				'EMPRESA: VIAÇÃO EXPRESSO UNIÃO / PLUMA - GUICHÊ: 25\n\nCONTATO: (32) 99177-0200\n\nSITE: https://www.expressouniao.com.br\n' 
				'FUNCIONAMENTO:\nseg - sex 08h - 18h\nsab dom feriados 14h30 - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 29\n\n'
				'TARIFA DE EMBARQUE R$5,25'
		   )
		#
        #
        #  VIAÇÃO UNICA FACIL:
        #
        elif nome in cidade_13 and nome in tarifa_3:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14 =-=-=-\n\nCONTATOS:\nCentral: (24)2244-1642 ou (24)2244-1600 (GARAGEM)\nPANTUR: 3216-2975\n' 
				'SITE: http://www.unicafacil.com.br/\nFUNCIONAMENTO: seg à sab: 05h40 - 18h30 dom: 05h40 à 17h40\nPLATAFORMA:19\n\n'
				'TARIFA DE EMBARQUE R$2,55'
            )
        #
        #
        #  VIAÇÃO UNICA FACIL:
        #
        elif nome in cidade_13 and nome in tarifa_4:
           resultado = (
			   '=-=-=- EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14 =-=-=-\n\nCONTATOS:\nCentral: (24)2244-1642 ou (24)2244-1600 (GARAGEM)\nPANTUR: 3216-2975\n' 
				'SITE: http://www.unicafacil.com.br/\nFUNCIONAMENTO: seg à sab: 05h40 - 18h30 dom: 05h40 à 17h40\nPLATAFORMA:19\n\n'
			   'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        #   VIAÇÃO JOSÉ MARIA RODRIGUES:
        #
        elif nome in cidade_14 and nome in tarifa_1:
            resultado = (
				'-=- EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07 -=-\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n' 
				'SITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n'
				'PLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO\n\n'
				'TARIFA DE EMBARQUE R$0,85'
			)
        #
        #
        #   VIAÇÃO JOSÉ MARIA RODRIGUES:
        #
        elif nome in cidade_14 and nome in tarifa_2:
            resultado = (
				'-=- EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07 -=-\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n' 
				'SITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n' 
				'PLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO\n\n'
				'TARIFA DE EMBARQUE R$1,45'
			)
        #
        #
        #   VIAÇÃO JOSÉ MARIA RODRIGUE:
        #
        elif nome in cidade_14 and nome in tarifa_3:
            resultado = (
				'-=- EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07 -=-\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n' 
				'SITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n' 
				'PLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO\n\n'
				'TARIFA DE EMBARQUE R$2,55'
		)
        #
        #
        #   VIAÇÃO ÀGUIA BRANCA:
        #
        elif nome in cidade_15 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO ÀGUIA BRANCA - GUICHÊ 26\n\nCONTATO:(32) 98710-6414\nSITE: https://www.aguiabranca.com.br\n' 
				'FUNCIONAMENTO:seg - sex 09h - 18h\nsab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 12\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        #
        #
        # VIAÇÃO ITAPEMIRIM / KAISSARA:
        #
        elif nome in cidade_16:
            resultado = (
				'EMPRESA: VIAÇÃO ITAPEMIRIM / KAISSARA - GUICHÊ: 29\n\nCONTATOS: (32) 3215-5020 \n0800 723 2121\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h\ndom 07h - 22h\n\nPLATAFORMA: 28\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
		#
        # VIAÇÃO BRASIL BUS:
        #
        if nome in cidade_17 and nome in tarifa_3:
            resultado = (
               'EMPRESA: VIAÇÃO "brasil bus" - GUICHÊ: 25\n\nCONTATO: (32) 99177-0200\n' 
				'FUNCIONAMENTO:\nseg - sex 08h - 18h\nsab dom feriados 14h30 - 18h (Intervalo: 12h30 - 13h30)\nPLATAFORMA: 29\n\n'
				'TARIFA DE EMBARQUE R$2,55' 
			)
        #
        if nome in cidade_17 and nome in tarifa_4:
            resultado = (
               'EMPRESA: VIAÇÃO "brasil bus" - GUICHÊ: 25\n\nCONTATO: (32) 99177-0200\n' 
				'FUNCIONAMENTO:\nseg - sex 08h - 18h\nsab dom feriados 14h30 - 18h (Intervalo: 12h30 - 13h30)\nPLATAFORMA: 29\n\n'
				'TARIFA DE EMBARQUE R$5,25' 
			)
        #
        #
        #   VIAÇÃO RODE ROTAS:
        #
        elif nome in cidade_18 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO RODE ROTAS - GUICHÊ 26\n\nCONTATO:(32) 98710-6414\n' 
				'FUNCIONAMENTO:seg - sex 09h - 18h\nsab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: "CONFIRMAR LOCAL DE EMBARQUE NO GUICHÊ"\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        #
		######################################################################################################################################################################
		#
		# LISTA DE ORGÃOS PÚBLICOS,LOJAS, SERVIÇOS E GUICHÊS NO INTERIOR DO TRJF:
		#
        elif nome == 'inss' or nome == 'previdencia' or nome == 'previdência' or nome == 'previdência social':
            resultado = (
				'-=-=-= AGÊNCIA INSS TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=\n\nATENDIMENTO: seg à sex de 07h àS 13h\nAGENDAMENTO: gov.br/meuinss ou 135'
			)
		#
        elif nome == 'conselho tutelar' or nome == 'juizado de menores' or nome == 'juizado menores':
            resultado = (
				'-=-=-= AGÊNCIA DO CONSELHO TUTELAR NO TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=\n\n'
				'ATENDIMENTO: seg à sex de 08h ás 12h e de 14h às 18h\n' 
				'CONTATO: (32)3690-7398\nATENDIMENTO DE PLANTÃO: (32)98429-4740'
			)
		#
        elif nome == 'smu':
            resultado = (
				'-=-=-= AGÊNCIA SMU TERMINAL RODOVIÁRIO MIGUEL MANSUR-=-=-=\n\n' 
				'ATENDIMENTO: seg à sex de 08h às 11h e de 14h às 17h\n' 
				'CONTATOS:\n\n SMU TAXI = (32)3690-2806\nSMU VANS ESCOLARES = (32) 3690-1811\n'
				'SMU VANS ESCOLARES ZONA RURAL = (32) 3690-2607'
			)
		#
        elif nome == 'antt':
            resultado = (
				'=-=-=- AGÊNCIA ANTT TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=\n\n' 
				'ATENDIMENTO: "PROVISORIAMENTE SUSPENSO!!!"\n\n' 
				'CONTATO: 166 (OUVIDORIA)'
			)
		#
        elif nome == 'guarda municipal' or nome == 'gm':
            resultado = (
				'-=-==-=-=-= GUARDA MUNICIPAL DE JUIZ DE FORA -=-=-=-=-=-=\n\n' 
				'CONTATO: 153 ou (32) 3690-7137'
			)
		#
        elif nome == 'cargas util' or nome == 'util cargas':
            resultado = (
				'-=-=-= CARGAS UTIL TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=\n\n' 
				'ATENDIMENTO: seg à sex de 08h às 18h - sáb 08h à 12h\n' 
				'RESPONSÁVEL: WAGNER ou VIVIAN\n\n' 
				'CONTATOS: (32)99828-0380'
			)
		#
        elif nome == 'encomendas ceu' or nome == 'ceu encomendas' or nome == 'ceu' or nome == 'andré' or nome == 'andre' or nome == 'André' or nome == 'Andre':
            resultado = (
				'-=-=-=-=-=-= CEU ENCOMENDAS TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=-=-=-=\n\n' 
				'ATENDIMENTO: seg à sex de 08h:30 às 17h\n' 
				'CONTATO-WHATSAPP (32)98831-3602\n\n'
				'RESPONSÁVEL: ANDRÉ'
			)
		#
        elif nome == 'cargas resendense' or nome == 'resendense cargas' or nome == 'resendense':
            resultado = (
				'-=-=-= CARGAS RESENDENSE TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=\n\n' 
				'ATENDIMENTO: seg à sex de 08h:30 às 12h\n' 
				'CONTATOS: (32)3084-4346 - https://resendensecargas.spaceblog.com.br\n\n'
				'RESPONSÁVEL: RESENDE'
			)
		#
        elif nome == 'edimar despachante' or nome == 'edimar' or nome == 'despachante':
            resultado = (
				'-=-=-=-=-=-= EDIMAR DESPACHANTE TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=-=-=-=\n\n' 
				'ATENDIMENTO: seg à sex de 07h às 18h\n\nCONTATOS: (32)99175-3064\n\n'
				'RESPONSÁVEL: EDIMAR'
			)
		#
        elif nome == 'migração' or nome == 'migracao' or nome == 'migraçao' or nome == 'centro pop' or nome == 'centropop':
            resultado = (
				'-=-=-=-=-=-= MIGRAÇÃO TERMINAL RODOVIÁRIO MIGUEL MANSUR -=-=-=-=-=-\n\n' 
				'ATENDIMENTO: seg à qui de 09h às 15h - sex de 13h às 15h\n'
				'CONTATOS: (32)3690-7102\n\nCENTRO POP - RUA SETE DE SETEMBRO 1341 (CENTRO)\n\n' 
				'FUNCIONAMENTO: 06h:30 Às 18h'
			)
		#
        elif nome == 'balcão' or nome == 'balcao' or nome == 'amd' or nome == 'amd balcão' or nome == 'amd balcao' or nome == 'rodoviaria' or nome == 'balcao rodoviaria' or nome == 'amd services':
            resultado = (
				'_-_-_- AMD SERVICES BALCÃO DE INFORMAÇÕES _-_-_-\n' 
				'=-=-=- TERMINAL RODOVIÁRIO MIGUEL MANSUR =-=-=-\n\nATENDIMENTO: seg à seg 24h\n' 
				'CONTATOS:\n(32) 3017-2828\n(32) 3313-4433\nWhatsApp: (32) 98848-8888\n\n' 
				'Av. Brasil nº 9501 Bairro São Dimas Cep: 36080-060'
			)
		#
        elif nome == 'adm' or nome == 'secretaria' or nome == 'administração' or nome == 'administraçao' or nome == 'administracao' or nome == 'adm amd' or nome == 'secretaria' or nome == 'diretoria':
            resultado = (
				'*-=-=-=-=-=-=-ADMINISTRATIVO TERMINAL RODOVIÁRIO MIGUEL MANSUR-=-=-=-=-=-=-*\n\n' 
				'ATENDIMENTO: seg à sex 9h às 18h\nEndereço: Av Brasil nº 9501, Bairro São Dimas Cep: 36080-060\n\n' 
				'****** (OBS: FAVOR ANOTAR RECADO, CASO SEJA FINAL DE SEMANA OU FERIADO) ******'
			)
		#
        elif nome == 'mensalista' or nome == 'estacionamento' or nome == 'mensalidade estacionamento' or nome == 'estacionamento pago' or nome == 'estacionamento mensalista':
            resultado = (
				'=-=-=- MENSALISTA ESTACIONAMENTO =-=-=-\n\n'
				'Documentos Necessários:\n> CNH\n> Documento do veículo\n> Comprovante de residência\n> Contatos (telefone e e-mail)\n\n'
				'Valor da mensalidade: R$ 145,00\n\nPermanência: Mínimo de 03 meses\n\nProcurar o setor ADMINISTRATIVO da AMD ASERVICES seg a sex de 9h às 18h'
			)
		#
        elif nome == 'rei do mate' or nome == 'rdm' or nome == 'rm':
            resultado = (
				'-=-=-= LANCHONETE REI DO MATE -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: 24h (exceto nas madrugadas de sab para dom)\n' 
				'Contato: (32) 99958-2881\n\nResponsável: Fabiano')
		#
        elif nome == 'cacau show' or nome == 'cacau' or nome == 'chocolateria' or nome == 'cs':
            resultado = (
				'-=-=-= CACAU SHOW -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: seg à seg 06h às 23h\n' 
				'Contato: (32) 99822-6153\n\nResponsável: Fabiano'
			)
		#
        elif nome == 'livraria nobel' or nome == 'livraria' or nome == 'nobel' or nome == 'nobel livraria':
            resultado = (
				'-=-=-= LIVRARIA NOBEL -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: seg à seg 06h às 23h\n' 
				'Contato: (32) 99828-7634\n\nResponsável: Fabiano'
			)
		#
        elif nome == 'empório rural' or nome == 'empório' or nome == 'emporio rural' or nome == 'emporio' or nome == 'rural':
            resultado = (
				'-=-=-= EMPÓRIO RURAL -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: 08h às 19h\n' 
				'Contato: "NÃO INFORMADO!"\nResponsável: Neiva'
			)
		#
        elif nome == 'bomboniere'  or nome == 'bombonier' or nome == 'bombonie' or nome == 'bomboniere vitória' or nome == 'bomboniere vitoria' or nome == 'vitória' or nome == 'vitoria':
            resultado = (
				'-=-=-= BOMBONIERE VITÓRIA -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: dom à dom 05h e 30 às 22h\n' 
				'Contato: "NÃO INFORMADO!"\n\nResponsável: Côrrea'
			)
		#
        elif nome == 'pastelaria' or nome == 'princesa dos pasteis' or nome == 'princesa dos pastéis' or nome == 'pastelaria correa' or nome == 'pastelaria côrrea' or nome == 'pastelariacorrea':
            resultado = (
				'-=-=-= PASTELARIA PRINCESA DOS PASTÉIS -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: 24h por dia 7 dias da semana\n' 
				'Contato: "NÃO INFORMADO!"\nResponsável: Côrrea'
			)
		#
        elif nome == 'lanchonete' or nome == 'santa lúcia' or nome == 'lsl' or nome == 'santa lucia' or nome == 'lanchonete santa lucia' or nome == 'snt lúcia' or nome == 'snt lucia' or nome == 'mercantil oliveira e côrrea' or nome == 'mercantil oliveira e correa' or nome == 'santalucia':
            resultado = (
			'-=-=-= LANCHONETE SANTA LÚCIA -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: dom à dom 05h e 30 às 22h\n' 
			'Contato: "NÃO INFORMADO!"\n\nResponsável: Côrrea'
		)
		#
        elif nome == 'farmácia' or nome == 'farmacia' or nome == 'farmaciaki' or nome == 'farmacia farmaciaki' or nome == 'farmaciaki farmacia':
            resultado = (
				'-=-=-= FARMÁCIA =-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nTEMPORARIAMENTE NÃO HÁ FARMÁCIA NO TERMINAL RODOVIÁRIO'
			)
		#
        elif nome == 'poderosa' or nome == 'loja poderosa' or nome == 'poderosa loja' or nome == 'poderosa presentes' or nome == 'loja poderosa presentes' or nome == 'lpp' or nome == 'poderosapresentes':
            resultado = (
				'-=-=-= PODEROSA PRESENTES -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n' 
				'Funcionamento: seg à seg 7h às 20h\nContato: (32) 3214-1310 (WHATS APP)\n\nResponsável: "PAULO JÚNIOR"'
			)
		#
        elif nome == 'belinha' or nome == 'belinha eletrônicos' or nome == 'belinha eletronicos' or nome == 'belinhaeletrônicos' or nome == 'belinhaeletronicos' or nome == 'eletronicos' or nome == 'eletrônicos':
            resultado = (
				'-=-=-= BELINHA ELETRÔNICOS -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: seg à seg 7h às 20h\n' 
				'Contato: (32) 3212-8042\n\nRESPONSÁVEL: MAURO'
			)
		#
        elif nome == 'padaria' or nome == 'estacao mineira' or nome == 'estação mineira' or nome == 'estaçao mineira':
            resultado = (
				'-=-=-= PADARIA ESTAÇÃO MINEIRA -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n' 
				'Funcionamento: 24h (exceto nas madrugadas de sab para dom)\nContato: (**) *****-****\nResponsável: Wagner / Adriana'
			)
		#
        elif nome == 'box100' or nome == 'box 100' or nome == 'box':
            resultado = (
				'-=-=-= BOX 100 GUARDA VOLUMES -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\nFuncionamento: 24h\nContatos:\n' 
				'AEROPORTO: (32) 3222-9015\nCENTRO: (32) 3026-2100 \nMARIANO: (32) 99198-0199\n\nResponsável: Ramiro (32) 98808-5534'
			)
		#
        elif nome == 'centertour' or nome == 'center tour' or nome == 'CENTER TOUR' or nome == 'centertur' or nome == 'centetur' or nome == 'center tu' or nome == 'center tur':
            resultado = (
				'-=-=-= AGÊNCIA CENTER TOUR -=-=-=\n\nLocal: Rua Halfeld 608/110 - Centro de Juiz de Fora\n' 
				'CEP: 36070-010 - Galeria Zé Kodak\nFuncionamento: seg a sex: 08h30 às 18h - sab: 08h30 às 13h\n' 
				'Contatos: (32) 3025-3936\n\nResponsável: NÃO INFORMADO!'
			)
		#
		######################################################################################################################################################################
		#
		#GLOSSÁRIO TERMINAL RODOVIÁRIO...
		#
        elif nome == 'p1' or nome == 'p 1' or nome == 'p01' or nome == 'p 01':
            resultado = (
				'P1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nENTRADA PRINCIPAL DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\n' 
				'ABRANGÊNCIA: TERMINAL DO PONTO DE ÔNIBUS URBANO À CAPELA\n' 
				'E LOJAS DA ENTRADA DO TERMINAL RODOVIÁRIO.'
			)
		#
        elif nome == 'p2' or nome == 'p 2' or nome == 'p02' or nome == 'p 02':
            resultado = (
				'P2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nSAÍDA PRINCIPAL DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\n' 
				'ABRANGÊNCIA: CORRENTE DE ENTRADA DO CARGA E DESCARGA\n' 
				'AO CORREDOR DOS FUNDOS PRÓXIMO A SUBSTAÇÃO DE ENERGIA'
			)
		#
        elif nome == 'p3' or nome == 'p 3' or nome == 'p03' or nome == 'p 03':
            resultado = (
				'P3 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nSETOR DE DESEMBARQUE DE PASSAGEIROS\n' 
				'NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\n' 
				'ABRANGÊNCIA: PLATAFORMAS DE 1 À 8'
				)
		#
        elif nome == 'p4' or nome == 'p 4' or nome == 'p04' or nome == 'p 04':
            resultado = (
				'P4 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO SETOR DE EMBARQUE DE PASSAGEIROS\n'
				'NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\n' 
				'ABRANGÊNCIA: PLATAFORMAS DE 9 À 31\n' 
				'PASSANDO PELAS CATRACAS DE EMBARQUE'
			)
		#
        elif nome == 'p5' or nome == 'p 5' or nome == 'p05' or nome == 'p 05':
            resultado = (
				'P5 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nSANITÁRIOS (PAGOS E GRATUITOS\n'
				'NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA'
			)
		#
        elif nome == 'p6' or nome == 'p 6' or nome == 'p06' or nome == 'p 06':
            resultado = (
				'P6 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nADMINISTRAÇÃO DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n' 
				'NO P6 SE ENCONTRAM OS SETORES DE ENGENHARIA E TÉCNICOS DA AMD SERVICES\n'
				'SETOR DE R-AFIS, SALA DOS SUPERVISORES, SECRETARIA, E DIRETORIA DA AMD'
			)
		#
        elif nome == 'p7' or nome == 'p 7' or nome == 'p07' or nome == 'p 07':
            resultado = (
				'P7 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nESTACIONAMENTO PAGO DO TERMINAL RODOVIÁRIO EM JUIZ DE FORA\n\n' 
				'EM CASO DE DÚVIDAS SOBRE ADESÃO DE NOVOS MENSALISTAS:\n' 
				'PESQUISAR PELA PALAVRA CHAVE\n\n>>> "MENSALISTA" <<<'
			)
		#
        elif nome == 'p8' or nome == 'p 8' or nome == 'p08' or nome == 'p 08':
            resultado = (
				'P8 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nREFEITÓRIO FUNCIONÁRIOS AMD SERVICES NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA'
			)
		#
        elif nome == 'p9' or nome == 'p 9' or nome == 'p09' or nome == 'p 09':
            resultado = (
				'P9 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE DO ALMOXARIFADO\n' 
				'NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA'
			)
		#
        elif nome == 'alfa1' or nome == 'alfa 01' or nome == 'alfa 1' or nome == 'alpha1' or nome == 'alpha 1':
            resultado = (
				'ALPHA 1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO GERENTE OPERACIONAL\n' 
				'DO TERMINAL RODOVIÁRIO MIGUEL MANSUR EM JUIZ DE FORA.\n\n' 
				'RESPONSÁVEL: REGIVAN SILVA')
		#
        elif nome == 'alfa2' or nome == 'alfa 02' or nome == 'alfa 2' or nome == 'alpha2' or nome == 'alpha 2':
            resultado = (
				'ALPHA 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AOS SUPERVISORES DE EQUIPE DOS TURNOS "A", "B", "C", E "D"\n\n' 
				'RESPONSÁVEIS:\n\nJEFFERSON DOMINGOS (TURNO A)\nANA MARIA (TURNO B)\nSIDCLEI CHAVES (TURNO C)\nDAVIS PETERSON (TURNO D)'
			)
		#
        elif nome == 'alfa3' or nome == 'alfa 03' or nome == 'alfa 3' or nome == 'alpha3' or nome == 'alpha 3':
            resultado = (
				'ALPHA 3 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO BALCÃO DE INFORMAÇÕESn\n' 
				'SETOR PERTINENTE AOS "OPERADORES" DE NÍVEL OPERACIONAL\n'
				'EM FUNÇÕES LABORAIS DE ATENDIMENTO AO PÚBLICO EM GERAL.'
			)
		#
        elif nome == 'alfa4' or nome == 'alfa 04' or nome == 'alfa 4' or nome == 'alpha4' or nome == 'alpha 4':
            resultado = (
				'ALPHA 4 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nPROFISSIONAL RESPONSÁVEL POR DESEMPENHAR O SUPORTE\n' 
				'AOS SISTEMAS DE INFORMAÇÃO E SEGURANÇA DA INFORMAÇÃO NO TERMINAL\n' 
				'RODOVIÁRIO DE JUIZ DE FORA\n\n' 
				'RESPONSÁVEL: FABIANO LANDIM'
			)
		#
        elif nome == 'alfa5' or nome == 'alfa 05' or nome == 'alfa 5' or nome == 'alpha5' or nome == 'alpha 5':
            resultado = (
				'ALPHA 5=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nGERENTE ADMINISTRATIVO DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\n' 
				'RESPONSÁVEL: SARAH FAUSTINO'
			)
		#
        elif nome == 'alfa6' or nome == 'alfa 06' or nome == 'alfa 6' or nome == 'alpha6' or nome == 'alpha 6':
            resultado = (
				'ALPHA 6 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO PROFISSIONAL RESPONSÁVEL POR AUXILIAR\n' 
				'NAS DEMANDAS PERTINENTES À MANUTENÇÃO DO TERMINAL RODOVIÁRIO\n\n' 
				'RESPONSÁVEL: HUGO LAUREANO'
			)
		#
        elif nome == 'alfa7' or nome == 'alfa 07' or nome == 'alfa 7' or nome == 'alpha7' or nome == 'alpha 7':
            resultado = (
				'ALPHA 7 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO PROFISSIONAL RESPONSÁVEL POR DESEMPENHAR OS TRABALHOS\n'
				'DE MANUTEÇÃO NO TERMINAL RODOVIÁRIO\nRESPONSÁVEL: ROBERTO GONÇALVES'
			)
		#
        elif nome == 'alfa8' or nome == 'alfa 08' or nome == 'alfa 8' or nome == 'alpha8' or nome == 'alpha 8':
            resultado = (
				'ALPHA 8 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\nCÓDIGO REFERENTE AOS PROFISSIONAIS RESPONSÁVEIS EM VIGIAR\n' 
				'O FLUXO DE PESSOAS NO TRJFASSIM COMO OS BENS DA ENTIDADE'
				'TOMANDO AS MEDIDAS NECESSÁRIAS PARA SE  EVITAR DANOS PATRIMONIAIS\n' 
				'BASEANDO-SE NAS CIRCUNSTÂNCIAS OBSERVADAS E VALENDO-SE DA AUTORIDADE A QUAL LHES FORAM OUTORGADA'
			)
		#
        elif nome == 'alfa9' or nome == 'alfa 09' or nome == 'alfa 9' or nome == 'alpha9' or nome == 'alpha 9':
            resultado = (
                'ALPHA 9 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO PROFISSIONAL RESPONSÁVEL POR AUXILIAR O SETOR ADMINISTRATIVO DO TERMINAL RODOVIÁRIO\n\nRESPONSÁVEL: EDILSON SARMENTO'
		)
		#
        elif nome == 'alfa10' or nome == 'alfa 10' or nome == 'alfa 10' or nome == 'alpha9' or nome == 'alpha 10':
            resultado = (
				'ALPHA 10 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO PROFISSIONAL RESPONSÁVEL PELA MANUTENÇÃO\n'
                'E CONSERVAÇÃO DA JARDINAGEM NO TERMINAL RODOVIÁRIO\n\nRESPONSÁVEL: SÉRGIO'
			)
		#
        elif nome == 'alfa11' or nome == 'alfa 11' or nome == 'alfa 11' or nome == 'alpha11' or nome == 'alpha 11':
            resultado = (
				'ALPHA 10 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n\nCÓDIGO REFERENTE AO PROFISSIONAL ENCARREGADO DA EQUIPE DE MANUTENÇÃO\n' 
                'DO TERMINAL RODOVIÁRIO\n\nRESPONSÁVEL: LUIZ OTÁVIO'
			)
		#
		######################################################################################################################################################################
		#
		#RELAÇÃO DOS GUICHÊS E SEUS DADOS...
		#
		# VIAÇÃO SARITUR / COORDENADAS / ATUAL...
		#
        elif nome == 'saritur' or nome == 'Saritur' or nome == 'Coordenadas' or nome == 'coordenadas' or nome == 'Atual' or nome == 'atual':
            resultado = (
				'EMPRESA: VIAÇÃO COORDENADAS  -  ATUAL - SARITUR\n\nCONTATO: (32) 3112-0423 - GUICHÊS: 04 e 05\n' 
				'SITE: https://www.saritur.com.br/\n\nFUNCIONAMENTO: dom guanabaraa sex das 06h30 - 00h\nsab de 06h30 - 19h\n\nPLATAFORMA: 22'
			)
		#
		# VIAÇÃO UTIL / GUANABARA / GIPSYY / SAMPAIO / BRISA...
		#
        elif nome == 'util' or nome == 'brisa' or nome == 'guanabara' or nome == 'sampaio' or nome == 'gypsyy' or nome == 'rapido federal' or nome == 'rápido federal' or nome == 'rapidoferedal' or nome == 'real expresso' or nome == 'realexpresso':
            resultado = (
				'EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY\nGUANABARA / REAL EXPRESSO / RÁPIDO FEDERAL\n\n'
				'GUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830 - WHATSAPP:(32)98833-5497\n\nSITE:\n' 
				'UTIL: https://www.util.com.br/\nGUANABARA: https://www.viajeguanabara.com.br/\nSAMPAIO: https://viacaosampaio.com.br/\n\nPLATAFORMAS: 13, 14, e 15'
			)
		#
		# VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL...
		#
        elif nome == 'cometa' or nome == 'catarinense' or nome == 'expresso do sul' or nome == 'expressodosul' or nome == '1001':
            resultado = (
				'-=-=-= EMPRESA: VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001 -=-=-=\n\n' 
                'GUICHÊS 15 e 16 - CONTATO: 4004-9600 e 0800 942 0030\n\nSITE:\n' 
                'COMETA: https://www.cometa.com.br\nCATARINENSE: https://www.catarinense.com.br\n' 
                'EXPRESSO DO SUL: https://www.expressodosul.com.br\nVIAÇÃO1001: https://www.autoviacao1001.com.br\n' 
                'FUNCIONAMENTO: DIARIAMENTE 07h30 - 11h - 12h - 23h30\n' 
                'PLATAFORMAS: 10, 11 e 12\n'
			)
		#
		# VIAÇÃO PROGRESSO...
		#
        elif nome == 'progresso' or nome == 'viação progresso' or nome == 'viaçao progresso' or nome == 'viacao progresso' or nome == 'viaçãoprogresso':
            resultado = (
				'-=-=-=-= EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 -=-=-=-=\n\nCONTATOS:\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\nCENTER TOUR: (32) 3025-3936\nSITE: https://www.viacaoprogresso.com.br\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 25 e 26'
			)
		#
		# VIAÇÃO UNIDA...
		#
        elif nome == 'unida' or nome == 'viação unida' or nome == 'unida mansur' or nome == 'unidamansur':
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\nSITE: https://unidamansur.queropassagem.com.br\n' 
				'FUNCIONAMENTO: seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n\nPLATAFORMA: 23'
			)
		#
		# VIAÇÃO TRANSUR...
		#
        elif nome == 'transur' or nome == 'viação transur':
            resultado = (
				'EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10\n\nCONTATO: (32) 3218-3613\nSITE: https://https://www.transur.com.br/horarios_preco\n' 
				'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h\nter à  dom: 06h30- 12h - 13h -19h\n\nPLATAFORMA: 17'
			)
		#
		# VIAÇÃO BASSAMAR...
		#
        elif nome == 'bassamar' or nome == 'viação bassamar' or nome == 'viacao bassamar':
            resultado = (
				'EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31\n\nCONTATO: (32) 3215-5020\nSITE: https://www.viacaobassamar.queropassagem.com.br\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21'
			)
		#
		# VIAÇÃO RIO DOCE...
		#
        elif nome == 'rio doce' or nome == 'riodoce':
            resultado = (
				'EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\nSITE: http://www.viacaoriodoce.com.br/\n' 
				'FUNCIONAMENTO: DIARIAMENTE 07h - 21h30\n\nPLATAFORMA: 24'
			)
		#
		# VIÇÃO SANTA CRUZ...
		#
        elif nome == 'santa cruz' or nome == 'snta cruz'  or nome == 'sntacruz'  or nome == 'santacruz' or nome == 'sul minas' or nome == 'sulminas':
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\nSITE: https://viajesantacruz.com.br/\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMA:  16\n'
			)
		#
		# VIAÇÃO GONTIJO...
		#
        elif nome == 'gontijo' or nome == 'viação gontijo' or nome == 'viacao gontijo':
            resultado = (
				'=-=-=-=- EMPRESA: VIAÇÃO GONTIJO - GUICHÊ: 27 =-=-=-=-\n\nCONTATOS:\n(32) 3215-9458\n(32)98710-6414\nSITE: https://www.gontijo.com.br/\n' 
				'FUNCIONAMENTO: seg- sab 08h - 20h20\ndom - feriados 08h - 12h / 14h - 17h20\n\nPLATAFORMA: 27'
			)
		#
		# VIAÇÃO PARAIBUNA...
		#
        elif nome == 'paraibuna' or nome == 'viação paraibuna':
             resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\nSITE: https://www.paraibunatransportes.com.br/\n\nFUNCIONAMENTO:\nseg à qui: 05h45 - 10h30 - 11h30 às 18h\nsex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18'
			)
		#
		# VIAÇÃO UNIÃO...
		#
        elif nome == 'união' or nome == 'uniao' or nome == 'expresso união' or nome == 'expresso uniao' or nome == 'expressounião' or nome == 'expressouniao' or nome == 'pluma':
            resultado = (
				'EMPRESA: VIAÇÃO EXPRESSO UNIÃO / PLUMA / "brasil bus" - GUICHÊ: 25\n\nCONTATO: (32) 99177-0200\n\nSITE: https://www.expressouniao.com.br\n' 
				'FUNCIONAMENTO:\nseg - sex 08h - 18h\nsab dom feriados 14h30 - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 29'
			)
        #
        # VIAÇÃO BRASIL BUS:
        #
        elif nome == 'brasil bus' or nome == 'brasilbus':
            resultado = (
               'EMPRESA: VIAÇÃO "brasil bus" - GUICHÊ: 25\n\nCONTATO: (32) 99177-0200\n' 
				'FUNCIONAMENTO:\nseg - sex 08h - 18h\nsab dom feriados 14h30 - 18h (Intervalo: 12h30 - 13h30)\nPLATAFORMA: 29\n' 
			)
		#
		# VIAÇÃO UNICA...
		#
        elif nome == 'unica' or nome == 'viação unica' or nome == 'unica fácil' or nome == 'unica facil' or nome == 'unicafacil':
            resultado = (
				'EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14\n\nCONTATOS:\nCentral: (24)2244-1642 ou (24)2244-1600 (GARAGEM)\n' 
				'PANTUR: 3216-2975\n\nSITE: http://www.unicafacil.com.br/\nFUNCIONAMENTO: seg à sab: 05h40 - 18h30 dom: 05h40 à 17h40\n\nPLATAFORMA: 19'
			)
		#
		# VIAÇÃO JOSÉ MARIA RODRIGUES...
		#
        elif nome == 'josé maria rodrigues' or nome == 'jose maria rodrigues' or nome == 'josemariarodrigues' or nome == 'jmr':
             resultado = (
				'EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\nSITE: https://www.josemariarodrigues.com.br\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n\nPLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO")'
			)
		#
		# VIAÇÃO ÀGUIA BRANCA...
		#
        elif nome == 'águia branca' or nome == 'aguia branca' or nome == 'aguiabranca':
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO ÁGUIA BRANCA e RODE ROTAS - GUICHÊ 26 =-=-=-\n\nCONTATO:(32) 99177-0200\nSITE: https://www.aguiabranca.com.br\nFUNCIONAMENTO:\nseg - sex 09h - 18h\n	sab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 12'
			)
		#
		# VIAÇÃO ITAPEMIRIM...
		#
        elif nome  == 'itapemirim' or nome == 'viação itapemirim' or nome == 'kaissara':
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO ITAPEMIRIM / KAISSARA - GUICHÊ: 29 =-=-=-\n\n' 
				'CONTATOS: (32)3025-3936 - 08007700050\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h - dom 07h - 22h\n\n' 
				'PLATAFORMA: 28'
			)
        #
        # VIAÇÃO RODE ROTAS...
		#
        elif nome == 'RODE ROTAS' or nome == 'RODEROTAS' or nome == 'rode rotas' or nome == 'roderotas':
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO RODE ROTAS - GUICHÊ 26 =-=-=-\n\nCONTATO:(32) 99177-0200\nFUNCIONAMENTO:\nseg - sex 09h - 18h\nsab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 12 ou BR 040 - GRAALL SILVIOS'
			)
		#
        # Atualiza a área de saída
        self.output.text = resultado

    def limpar(self, instance):
        """Limpa o campo de entrada e a área de saída."""
        self.input.text = ""
        self.output.text = ""
    def sair(self, instance):
        """Fecha o aplicativo."""
        App.get_running_app().stop()

if __name__ == "__main__":
    MainApp().run()
