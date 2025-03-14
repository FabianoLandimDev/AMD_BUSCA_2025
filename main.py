from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


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
# v1.0.6_2025_03_14, Fabiano Landim
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
cidade_4 = ['afonso arinos', 'além paraíba', 'alem paraiba', 'além paraiba', 'alem paraíba', 'barra mansa', 'barra do piraí', ' bdp', 'barra do pirai', 'levy gasparian', 'matias barbosa', 'miguel pereira', 'miracema', 'paraíba do sul', 'paraiba do sul', 'pds', 'pirapitinga', 'serraria', 'três rios', 'tres rios', '3 rios', 'vassouras', 'volta redonda']
#
# VIAÇÃO SARITUR / COORDENADAS:
#
cidade_1 = ['bh', 'belo horizonte', 'betim', 'carandaí', 'carandai', 'congonhas', 'conselheiro lafayete', 'barbacena', 'congonhas', 'contagem', 'itaúna', 'itauna', 'mariana', 'natal', 'ouro preto', 'pará de minas', 'para de minas', 'pdm', 'raposo', 'ressaquinha',]
#
# VIAÇÃO UTIL/ BRISA/ SAMPAIO:
#
cidade_2 = ['angra dos reis', 'adr', 'brasília', 'brasilia', 'caxias', 'conservatória', 'conservatoria', 'gurupi', 'gurupí', 'imperatriz', 'macaé', 'macae', 'madureira', 'rdj', 'rio de janeiro', 'rio', 'rj', 'valença', 'valenca', 'manoel duarte', 'mogi das cruzes', 'mdc', 'niterói', 'niteroi', 'ouro branco', 'parati', 'pernambuco', 'rio das flores', 'rdf', 'rio das ostras', 'rdo', 'são bernardo do campo', 'sao bernardo do campo', 'sbdc', 'são josé dos campos', 'sao jose dos campos', 'sjdc', 'taubaté', 'taubate', 'valença', 'valenca']
#
# VIAÇÃO UNIDA:
#
cidade_5 = ['caranguejo', 'coimbra', 'coronel fabriciano', 'ervália', 'ervalia', 'ipatinga', 'itabira', 'joão molevade', 'joao molevade', 'molevade',  'mercês', 'merces', 'nova era', 'ponte nova', 'porto firme', 'rio casca', 'rio pomba', 'são domingos do prata', 'sao domingos do prata', 'sddp', 'são geraldo', 'sao geraldo', 'senador firmino', 'tabuleiro', 'teixeiras', 'timóteo', 'timoteo', 'tocantins', 'ubá', 'uba', 'viçosa', 'vicosa', 'visconde do rio branco', 'vdrb']
#
# VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001:
#
cidade_3 = ['alfenas', 'águas de lindóia', 'aguas de lindoia', 'adl', 'americana', 'aparecida do norte', 'ap do norte', 'adn', 'bragança paulista', 'braganca paulista', 'campinas', 'campo mourão', 'campo mourao', 'sp', 'são paulo', 'sao paulo', 'araraquara', '*catanduvas', 'curitiba', 'extrema', 'florianópolis',  'florianopolis', 'floripa', 'jacareí', 'jacarei', 'joinvile', 'jundiaí', 'jundiai', 'londrina', 'medianeira', 'mogi mirim', 'mogi guaçu', 'mogi guaçú', 'mogi guacu', 'ourinhos', '*piracicaba', 'pirassununga', 'porto alegre', 'resende', '*ribeirão preto', '*ribeirao preto', 'santo andré', 'santo andre', 'santos', 'são caetano', 'sao caetano', 'são carlos', 'sao carlos', 'são gonçalo do sapucaia', 'sao gonçalo do sapucaia', 'sgds', 'são joão do rio preto', 'sao joao do rio preto', 'sjdrp', 'sorocaba']
#
# VIAÇÃO TRANSUR:
#
cidade_6 = ['bananal', 'barbacena', 'barroso', 'caieiro', 'correia de almeida', 'cda', 'dores de campos', 'ddc', 'ewbank da câmara', 'ewbank da camara', 'edc', 'faixa azul', 'helvas', 'ibertioga', 'itutinga', 'lavras', 'madre de deus', 'mdd',  'peróbas', 'perobas', 'prados', 'santos dumont', 'são joão da serra', 'sjds', 'sao joao da serra', 'são joão del rei', 'sao joao del rei', 'sjdr', 'são sebastião da vitória', 'sao sebastiao da vitoria', 'ssdv', 'tiradentes']
#
# VIAÇÃO BASSAMAR:
#
cidade_7 = ['aeroporto', 'acampamento de campelina', 'andrelândia', 'arantina', 'argirita - conexão', 'bela vista de minas', 'bias fortes', 'bicas', 'boa vista', 'bom jardim de minas - conexão', 'br 267 - guarará', 'cachoeira', 'chiador', 'conceição', 'conceição do rio verde', 'conceicao do rio verde', 'conceiçao do rio verde', '*conceição do monte alegre', '*conceiçao do monte alegre', 'coronel pacheco - conexão', 'cristais - conexão', 'descoberto', 'fazenda vitória - conexão', 'ferreira lage', 'guarará',  'goianá - conexão', 'goiana - conexão', 'joao ferreira - conexão', 'joão ferreira - conexão', 'leopoldina - conexão', '*liberdade', 'lima duarte', 'mar de espanha', 'maripa de minas - conexão', 'monte verde', 'olaria', 'orvalho', 'palmital', 'passo pátria', 'passo patria', 'passopatria', 'pedro teixeira', 'pequeri', 'ponte preta - conexão', 'recreio',  'rio novo - conexão', 'rio preto', 'rochedo de minas', 'santa bárbara', 'snt bárbara', 'santa barbara', 'santa helena de minas - conexão', 'santa rita do jacutinga',  'snt rita do jacutinga', 'santana do deserto', 'santo antônio aventureiro', 'santo antonio aventureiro', 'são joão nepomuceno', 'sao joao nepomuceno', 'são roque de minas', 'sao roque de minas', 'são vicente de minas', 'sao vicente de minas', 'senador cortês', 'senador cortes', 'serra bocaina - conexão', 'sossego', 'tebas - conexão', 'torres', 'três ilhas', 'tres ilhas', '3 ilhas', 'valadares', 'vale sobrado']
#
# VIAÇÃO RIO DOCE:
#
cidade_8 = ['águas pretas', 'aguas pretas', 'almenara', 'araçuaí', 'bicas-trevo', 'bicuíba', 'bom jesus do itabapoana', 'cachoeiro de itapemirim', 'cachoeiro de itapemirim', 'camacã', 'camacan', 'campanário', 'campos dos goytacazes', 'campos', 'caratinga', 'carlos chagas', 'dom cavate', 'engenheiro caldas', 'eng caldas', 'eunápolis', 'eunapolis', 'felisburgo', 'frei inocêncio', 'frei inocencio', 'governador valadares', 'guarapari', 'guaraparí', 'ilhéus', 'ilheus', 'inhapim', 'itabacuri', 'itabuna', 'itagimirim', 'itamaraju', 'itambé', 'itambe', 'itaobim', 'itaoca', 'itaperuna',  'jequitinhonha', 'leopoldina - conexão*', '*manhuaçu', '*manhuacu', 'marataizes', 'marataízes', 'monte pascoal', 'nanuque', 'novo cruzeiro', 'orizânia', 'orizania', 'pedra azul', 'piúma', 'piuma', 'posto da mata', 'realeza', 'rio do prado', 'santa bárbara do leste', 'santa barbara do leste', 'snt barbara do leste', 'santa clara', 'snt clara', 'teófilo otoni', 'teofilo otoni',  'vargem grande', 'vila velha', 'virgem da lapa', 'vdl', 'vitória', 'vitoria', 'vitória da conquista', 'vitoria da conquista']
#
# VIAÇÃO SANTA CRUZ:
#
cidade_9 = ['aiuruoca', '*alfenas', '*americana', 'andradas', '*araraquara', 'baependi', 'bom jardim de minas', '*bragança paulista', 'cambuquira', '*campinas', 'carvalhos', 'catanduvas', 'caxambu', 'cruzilia', 'cruzília', 'guaxupé', 'guaxupe', 'lambari', 'passa quatro', 'piracicaba', '*pirassununga', 'poços de caldas', 'pocos de caldas', 'pouso alegre', 'ribeirão preto', 'ribeirao preto',  '*são carlos', '*sao carlos', 'são josé do rio preto', 'sao jose do rio preto', 'sjrp', '*são joão do rio preto', 'sao joao do rio preto', 'são lourenço', 'sao lourenço', 'sao lourenco', 'são tomé das letras', 'sao tome das letras', 'seritinga', 'três corações', 'tres coraçoes', 'tres coracoes', 'varginha', ]
#
# VIAÇÃO GONTIJO:
#
cidade_10 = ['alto araguaia', 'alto garças', 'anápolis', 'anapolis', 'aracajú', 'araxá', 'arcos', 'bambuí', 'bom despacho', 'campo belo', 'campos altos', 'cana verde', 'candeias', 'catalão', 'cristais', 'cuiabá', 'divinópolis', 'divinopolis', 'estalagem', 'feira de santana', 'fds', 'formiga', 'iguatama', 'itumbiara', 'jaciara', 'jataí', 'jequié', 'joão pessoa', 'joao pessoa', 'mineiros', 'nova ponte', 'nova serrana', 'oliveira', 'perdões', 'perdoes', 'rio verde', 'rondonópolis', 'rondonopolis', 'santa juliana', 'snt juliana', 'uberaba', 'uberlândia', 'uberlandia']
#
# VIAÇÃO PARAIBUNA:
#
cidade_11 = ['alto jequitibá', 'alvorada de minas', 'argirita', 'bom jesus da cachoeira', 'caparaó divino', 'carangola', 'cataguases', 'conceição do monte alegre', 'espera feliz', 'fervedouro', 'fortaleza de minas', '*guarará', 'laranjal', 'leopoldina', 'liberdade', 'manhuaçu', 'manhumirim', 'maripá de minas', '*matias barbosa', 'mindurí', '*miguel pereira', 'miradouro', 'miraí', '*monte verde', 'muriaé', 'parque nacional caparaó', 'passo da pátria', 'ponte preta', 'santa helena de minas', 'serra bocaina', 'simão pereira', '*sossego', 'tebas']
#
# VIAÇÃO UNIÃO:
#
cidade_12 = ['alto paraíso de goiás', 'araguari', 'arraias', 'belém', 'bocaiúva', 'buenópolis', 'caldas novas', 'campos belos', 'conceição do tocantins', 'corinto', 'curvelo', 'goiânia', 'janaúba', 'jaraguá', 'jaragua', 'lages', 'mafra', 'maringá', 'medina', 'monte alegre de goiás', 'monte carmelo', 'montes claros', 'natividade', 'palmas', 'paracatu','paracatú', 'patos de minas', 'patrocínio', 'piracanjuba', 'pirapora', 'planaltina', 'porangatu', 'porto nacional', 'rialma', 'santa rosa do tocantins', 'santo ângelo', 'são gabriel', 'são joão daliança', 'são joão da aliança', 'sao joao da aliança', 'são luiz gonzaga', 'sete lagoas', 'silvanópolis', 'três marias', '3 marias', 'tres marias',  'unaí', 'uruaçú']
#
# VIAÇÃO UNICA:
#
cidade_13 = ['areal', 'búzios - conexão', 'buzios - conexão', 'cabo frio', 'itaipava', 'nova friburgo', 'nova iguaçú', 'petrópolis', 'rio bonito', 'são pedro da aldeia']
#
# VIAÇÃO JOSÉ MARIA RODRIGUES:
#
cidade_14 = ['aeroporto - conexão', 'astolfo dutra', 'bicas-conexão', 'campestre', 'coronel pacheco', 'dona euzébia', 'dona euzebia', 'goianá', 'goiana', 'guarani', 'guaraní', 'joão ferreira', 'joao ferreira', 'piau', 'piraúba', 'pirauba', 'rio novo', 'sobral pinto', 'toledos', 'triqueda']
#
# VIAÇÃO ÀGUIA BRANCA:
#
cidade_15 = ['foz do iguaçú', 'foz do iguaçu', 'foz do iguacu', 'são josé dos campos', 'sao jose dos campos', '*taubaté', '*taubate']
#
# VIAÇÃO ITAPEMIRIM:
#
cidade_16 = ['*aracaju', 'aracaju', '*aracajú', '*aracaju', '*belo horizonte', '*bh', 'campina grande', '*curitiba', '*feira de santana', '*fds', '*guarapari', '*guaraparí', '*ipatinga', '*nanuque', 'rio de janeiro - conexão' , 'salvador', 'são paulo - conexão', '*sao paulo', '*sp', '*vitória da conquista', '*vitoria da conquista', '*vdc']
#
# LISTA DE CIDADES POR TARIFAS:
#
# Referente ao valor da tarifa de R$0,85
#
tarifa_1 = ['aeroporto', 'aeroporto - conexão', 'goianá', 'goiana', 'goianá - conexão', 'goiana - conexão', 'conceição do rio verde', 'conceicao do rio verde', 'conceiçao do rio verde', 'coronel pacheco', 'coronel pacheco - conexão', 'ewbank da câmara', 'ewbank da camara', 'ewbank', 'eubank da camara', 'ferreira lage', 'joão ferreira', 'joao ferreira', 'joao ferreira - conexão', 'joão ferreira - conexão', 'matias barbosa', '*matias barbosa', 'monte verde', '*monte verde', 'passo da pátria', 'passo da patria', 'santa bárbara', 'snt bárbara', 'santa barbara', 'são roque de minas', 'sao roque de minas', 'senador cortês', 'senador cortes', 'triqueda', 'valadares'] 
#
# Referente ao valor da tarifa de R$1,45
#
tarifa_2 = ['afonso arinos', 'bela vista de minas', 'bias fortes', 'bicas', 'bicas-conexão', 'boa vista', 'bom jardim de minas', 'bom jardim de minas - conexão', 'br 267 - guarará', 'cachoeira', 'caranguejo', 'chiador', 'conceiçao', 'conceicao', 'conceição', 'correia de almeida', 'cristais - conexão', 'faixa azul', 'fazenda vitória - conexão', 'guarani', 'guaraní', 'guarará', 'guarara', '*guarará', '*guarara', 'lima duarte', 'mar de espanha', 'maripá de minas - conexão', 'maripa de minas - conexão', 'olaria', 'orvalho', 'palmital','paraíba do sul', 'paraiba do sul', 'passo pátria', 'passo patria', 'passopatria', 'pedro teixeira', 'pequeri', 'pequerí', 'peróbas', 'perobas', 'piau', 'ponte preta', 'ponte preta - conexão', 'rio novo', 'rio novo - conexão', 'rio pomba', 'rochedo de minas', 'santa helena de minas', 'santa helena de minas - conexão', 'snt helena de minas',  'santo antônio aventureiro', 'santos dumont', 'são joão da serra', 'sao joao da serra', 'são joão nepomuceno', 'sao joao nepomuceno', 'simão pereira', 'simao pereira', 'sossego', 'sôssego', '*sôssego', '*sossego', 'tabuleiro']
#
# Referente ao valor da tarifa de R$2,55
#
tarifa_3 = ['além paraíba', 'alem paraiba', 'além paraiba', 'alem paraíba', 'acampamento de campelina', 'alto jequitibá', 'alto jequitiba', 'alvorada de minas', 'argirita', 'argirita - conexão', 'astolfo dutra', 'barbacena', 'barroso', 'bom jesus da cachoeira', 'caieiro', 'campestre', 'carandaí', 'carandai', 'coimbra', 'ubá', 'uba', 'visconde do rio branco', 'cataguases', 'conceição do monte alegre', 'conceicao do monte alegre', '*conceição do monte alegre', '*conceicao do monte alegre', 'conservatória', 'conservatoria', 'descoberto', 'dona euzébia', 'dores de campos', 'ervália', 'ervalia', 'fortaleza de minas', 'helvas', 'ibertioga', 'itaipava', 'laranjal', 'levy gasparian', 'madre de deus', 'manoel duarte', 'mercês', 'merces', 'minduri', 'mindurí', 'miguel pereira', '*miguel pereira', 'nova friburgo', 'nova iguaçú', 'nova iguaçu', 'paraíba do sul', 'paraiba do sul', 'pds', 'petrópolis', 'petropolis', 'pirapitinga', 'piraúba', 'pirauba', 'prados', 'ressaquinha', 'rio das flores', 'rio preto', 'santana do deserto', 'são pedro da aldeia', 'sao pedro da aldeia', 'são sebastião da vitória', 'sao sebastiao da vitoria', 'senador firmino', 'serra bocaina', 'serra bocaina - conexão', 'sobral pinto', 'tebas - conexão', 'tebas', 'tiradentes', 'tocantins', 'toledos', 'três ilhas', 'tres ilhas', '3 ilhas', 'três rios',  'tres rios', '3 rios', 'vale sobrado', 'valença', 'vassouras', 'visconde do rio branco'] 
#
# Referente ao valor da tarifa de R$5,25
#
tarifa_4 = ['alegrete', 'aiuruoca', 'almenara', 'alfenas', '*alfenas', 'alto araguaia', 'alto garças', 'alto garcas', 'águas pretas', 'aguas pretas', 'águas de lindóia', 'aguas de lindoia', 'alto paraíso de goiás', 'alto paraiso de goias', 'americana', '*americana', 'anápolis', 'andradas', 'andrelândia', 'angra dos reis', 'aparecida do norte', 'aracajú', '*aracajú', '*aracaju', 'araçuaí', 'araguari', 'arantina', 'araraquara', '*araraquara', 'araxá', 'arcos', 'areal', 'arraias', 'baependi', 'bambuí', 'bananal', 'barra do piraí', 'barra mansa', 'belém', 'belo horizonte','*belo horizonte', '*bh', 'bh', 'betim', 'bicas-trevo', 'bicuíba', 'bicuiba', 'bocaiúva', 'bocaiuva', 'bom despacho', 'bom jesus do itabapoana', 'bragança paulista', '*bragança paulista', '*braganca paulista', 'brasilia', 'brasília', 'buenópolis', 'buenopolis', 'búzios - conexão', 'buzios - conexão', 'cabo frio', 'cachoeiro de itapemirim', 'cachoeiro de itapemirim', 'caldas novas', 'camacã', 'camacan', 'cambuquira', 'campanario', 'campanário', 'campinas', '*campinas', 'campina grande', 'campo belo', 'campos dos goytacazes', 'cdg', 'campos goytacazes', 'campos altos', 'campos belos', 'campo mourão', 'campo mourao', 'cana verde', 'candeias', 'caparaó divino', 'caparao divino', 'carangola', 'caratinga', 'carlos chagas', 'carvalhos', 'catalao', 'catalão', 'catanduvas', '*catanduvas', 'caxambú', 'caxias', 'conceição do tocantins', 'conceicao do tocantins','cdt', 'congonhas', 'conselheiro lafayete', 'contagem', 'corinto', 'coronel fabriciano', 'cruzilia', 'cruzília',  'cuiabá', 'cuiaba', 'curitiba', '*curitiba', 'curvelo', 'divinópolis', 'divinopolis', 'dom cavate', 'engenheiro caldas', 'eng caldas', 'espera feliz', 'estalagem', 'eunápolis', 'eunapolis', 'extrema', 'cristais', 'feira de santana', '*feira de santana', 'felisburgo', 'fervedouro', 'florianópolis', 'florianopolis', 'formiga', 'foz do iguaçu', 'foz do iguaçú', 'foz do iguacu', 'frei inocêncio', 'frei inocencio', 'goiania', 'goiânia', 'governador valadares', 'guarapari', 'guaraparí', '*guaraparí', '*guarapari', 'guaxupé', 'guaxupe',  'gurupi', 'guarupí', 'iguatama', 'ilhéus', 'ilheus', 'ipatinga', '*ipatinga', 'imperatriz', 'inhapim', 'itabacuri', 'itabacurí', 'itabira', 'itabuna', 'itagimirim', 'itamaraju', 'itambé', 'itaobim', 'itaoca', 'itaperuna', 'itaúna', 'itauna', 'itumbiara', 'itutinga', 'jacareí', 'jacarei', 'jaciara', 'janaúba', 'janauba', 'jaraguá', 'jaragua', 'jataí', 'jatai', 'jequié', 'jequie', 'jequitinhonha', 'joão molevade', 'joao molevade', 'joão pessoa', 'joao pessoa', 'joinvile', 'jundiaí', 'jundiai', 'lages', 'lambari', 'lambarí', 'lavras', 'leopoldina', 'leopoldina - conexão', 'leopoldina - conexão_2','liberdade', '*liberdade', 'londrina', 'macaé', 'macae', 'madureira', 'mafra', 'manhuaçu', '*manhuaçu', 'manhuacu', '*manhuacu', 'manhumirim', 'marataizes', 'mariana', 'maringá', 'medianeira', 'medina', 'mineiros', 'miracema', 'miradouro', 'miraí', 'mirai', 'mogi mirim', 'mogi das cruzes', 'mogi guaçu', 'mogi guaçú', 'monte alegre de goiás', 'monte alegre de goias', 'monte carmelo', 'monte pascoal', 'montes claros', 'muriaé', 'muriae', 'nanuque', '*nanuque', 'natal', 'natividade', 'niterói', 'niteroi', 'nova era', 'nova ponte', 'nova serrana', 'novo cruzeiro', 'oliveira', 'ourinhos', 'ouro branco', 'ouro preto', 'orizânia', 'orizania', 'palmas', 'paracatu' 'paracatú', 'pará de minas', 'pará de minas', 'parati', 'parque nacional caparaó', 'parque nacional caparao', 'passa quatro', ' passa 4', 'patos de minas', 'patrocínio', 'patrocinio', 'pedra azul', 'perdões', 'perdoes', 'pernambuco', 'piracanjuba', 'piracicaba', '*piracicaba', 'pirapora', 'pirassununga', '*pirassununga', 'piúma', 'piuma', 'planaltina', 'poços de caldas', 'ponte nova', 'porangatu', 'porangatú', 'porto alegre',  'porto firme', 'porto nacional', 'posto da mata', 'pouso alegre', 'raposo', 'realeza', 'recreio', 'resende', 'rialma', 'ribeirão preto', '*ribeirão preto','ribeirao preto', '*ribeirao preto', 'rio bonito', 'rio casca', 'rio das ostras', 'rdo', 'rio de janeiro', '*rio de janeiro', 'rj', '*rj', 'rio do prado', 'rio verde', 'rondonópolis', 'rondonopolis', 'santa bárbara do leste', 'santa clara', 'snt clara', 'santa juliana', 'snt juliana', 'santa rita de jacuting a', 'snt rita de jacutinga', 'santa rosa do tocantins', 'santo andré', 'santo andre', 'santo ângelo', 'santo angelo', 'santos', 'são bernardo do campo', 'sao bernanrdo do campo', 'são caetano', 'sao caetano' 'são carlos', '*são carlos', 'são domingos do prata', 'são gabriel', 'são geraldo', 'são gonçalo do sapucaia', 'são joão daliança', 'são joão del rei', 'são josé do rio preto', 'são joão do rio preto', 'são josé dos campos', 'são lourenço', 'são luiz gonzaga', 'slg', 'sp', 'são paulo', 'sao paulo', '*são paulo', '*sao paulo', '*sp', 'são tomé das letras', 'sao tome das letras', 'são vicente de minas', 'sao vicente de minas', 'seritinga', 'serraria', 'sete lagoas', 'silvanópolis', 'silvanopolis', 'sorocaba', 'taubaté', 'taubate', '*taubaté', '*taubate' 'teixeiras', 'teófilo otoni', 'teofilo otoni', 'timóteo', 'timoteo', 'torres', 'três corações', 'tres coraçoes', 'tres coracoes', '3 coraçoes', '3 coracoes', 'três marias', 'tres marias', '3 marias', 'uberaba', 'uberlândia', 'uberlandia', 'unaí', 'unai', 'uruaçu', 'uruaçú', 'vargem grande', 'varginha', 'viçosa', 'vicosa', 'vila velha', 'virgem da lapa', 'vitória', 'vitória da conquista', 'vitoria da conquista', '*vitória da conquista', '*vitoria da conquista', 'volta redonda']
#
#LISTA_GERAL:
#
lista_geral = ['inss', 'previdencia', 'previdência', 'previdência social', 'conselho tutelar',  'juizado de menores' , 'juizado menores', 'smu', 'antt', 'guarda municipal', 'gm', 'cargas util', 'util cargas', 'encomendas ceu', 'ceu encomendas', 'ceu', 'andré', 'andre', 'André', 'Andre', 'cargas resendense', 'resendense cargas', 'resendense', 'edimar despachante', 'despachante',  'migração', 'centro pop', 'centropop', 'balcão', 'balcao' , 'amd', 'amd balcão', 'rodoviaria', 'rodoviária', 'amd services', 'adm', 'secrretaria', 'diretoria', 'mensalista', 'estacionamento', 'estacionamento pago', 'estacionamento mensalista', 'rei do mate', 'rm', 'cacaushow', 'cs', 'cacau', 'chocolateria', 'emporio rural', 'empório rural', 'emporio', 'empório', 'rural', 'bomboniere', 'vitoria', 'vitória', 'bombonier', 'pastelaria', 'princesa dos pastéis', 'côrrea', 'lanchonete', 'santa lúcia', 'lanchonete santa lúcia', 'santalucia', 'snt lucia', 'farmácia', 'farmacia', 'poderosa', 'poderosa presentes', 'poderosa loja', 'poderosapresentes', 'belinha', 'eletrônicos', 'belinha eletrônicos', 'eletronicos', 'padaria', 'estação mineira', 'estacao mineira', 'box100', 'box 100', 'box', 'center tour', 'centertour', 'centertur', 'center tur', 'p1', 'p01', 'p 1', 'p 01', 'p2', 'p02', 'p 2', 'p 02', 'p3', 'p03', 'p 3', 'p 03', 'p4', 'p04', 'p 4', 'p 04', 'p5', 'p05', 'p 5', 'p 05', 'p6', 'p06', 'p 6', 'p 06', 'p7', 'p07', 'p 7', 'p 07','p8', 'p08', 'p 8', 'p 08', 'p9', 'p09', 'p 9', 'p 09', 'p1', 'p01', 'p 1', 'alfa1', 'alfa 01', 'alfa1', 'alpha1', 'alpha 1', 'alfa2', 'alfa 02', 'alfa2', 'alpha2', 'alpha 2', 'alfa3', 'alfa 03', 'alfa3', 'alpha3', 'alpha 3', 'alfa4', 'alfa 04', 'alfa4', 'alpha4', 'alpha 4', 'alfa5', 'alfa 05', 'alfa5', 'alpha5', 'alpha 5', 'alfa1', 'alfa 06', 'alfa6', 'alpha6', 'alpha 6', 'alfa7', 'alfa 7', 'alfa7', 'alpha7', 'alpha 7', 'alfa8', 'alfa 08', 'alfa8', 'alpha8', 'alpha 8', 'alfa9', 'alfa 09', 'alfa9', 'alpha9', 'alpha 9', 'alfa10', 'alfa 10', 'alfa10', 'alpha10', 'alpha 10', 'alfa11', 'alfa 11', 'alfa11', 'alpha11', 'alpha 11', 'saritur', 'coordenadas', 'atual', 'util', 'brisa', 'guanabara', 'sampaio', 'gypsyy', 'cometa', 'catarinense', 'expresso do sul', 'expressodosul', '1001', 'progresso', 'viaçãoprogresso', 'viacao progresso', 'viaçao progresso', 'unida', 'viação unida', 'viaçãounida', 'unidamanssur', 'unida manssur', 'transur', 'viação transur', 'bassamar', 'viacao bassamar', 'riodoce', 'rio doce', 'viação rio doce', 'santa cruz', 'snt cruz', 'sntcruz', 'santacruz', 'sulminas', 'sul minas', 'gontijo', 'viação gontijo', 'paraibuna', 'viação paraibuna', 'viação união', 'união', 'uniao', 'expresso união', 'pluma', 'viação pluma', 'viação unica', 'unica', 'unica fácil', 'unica facil', 'unicafacil', 'josé maria rodrigues', 'jmr', 'jose maria rodrigues', 'josemariarodrigues', 'águiabranca', 'águia branca', 'aguia branca', 'águiabranca', 'roderotas', 'rode rotas', 'itapemirim', 'viação itapemirim', 'kaissara', 'viação kaissara']
#
#
#
class MainApp(App):
    def build(self):
        self.combined_cidades = self.get_combined_cidades()
        self.title = "AMD BUSCA  -  v1.0.6_2025_03_05 / Desenvolvido por: Fabiano Landim"
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title = Label(
            text="\\\/// AMD BUSCA \\\///",
            font_size=24,
            size_hint_y=None,
            height=30,
            color=('blue')
        )
        layout.add_widget(title)
        
        self.input = TextInput(
            hint_text="PESQUISAR POR: (OUTROS RESULTADOS PARA A MESMA CIDADE, INSIRA * ANTES DO NOME)",
            font_size=18,
            size_hint_y=None,
            height=40
        )
        self.input.bind(text=self.update_suggestions)
        layout.add_widget(self.input)
        
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        search_button = Button(text="Pesquisar", on_press=self.pesquisar)
        clear_button = Button(text="Limpar", on_press=self.limpar)
        exit_button = Button(text="Sair", on_press=self.sair)
        button_layout.add_widget(search_button)
        button_layout.add_widget(clear_button)
        button_layout.add_widget(exit_button)
        layout.add_widget(button_layout)
        
        # Área de sugestões
        self.suggestions_grid = GridLayout(cols=1, spacing=2, size_hint_y=None)
        self.suggestions_grid.bind(minimum_height=self.suggestions_grid.setter('height'))
        scroll_suggestions = ScrollView(size_hint=(1, None), height=150)
        scroll_suggestions.add_widget(self.suggestions_grid)
        layout.add_widget(scroll_suggestions)
        
        # Área de saída
        scroll_view = ScrollView()
        self.output = Label(
            text="",
            font_size=18,
            size_hint_y=None,
            height=450,
            markup=True
        )
        scroll_view.add_widget(self.output)
        layout.add_widget(scroll_view)
        
        return layout

    def get_combined_cidades(self):
        return (
            cidade_1 + cidade_2 + cidade_3 + cidade_4 + cidade_5 + cidade_6 + cidade_7 +
            cidade_9 + cidade_10 + cidade_11 + cidade_12 + cidade_13 + cidade_14 + cidade_15 + cidade_16 + lista_geral
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
            btn = Button(text=match, size_hint_y=None, height=40, background_color=(0.95, 0.95, 0.95, 2))
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
        elif nome  in cidade_2 and nome  in tarifa_4:
            resultado = (
				'-=- EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY / GUANABARA -=-\n\n'
                'GUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830 - WHATSAPP:(32)98833-5497\n' 
                'SITE: UTIL: https://www.util.com.br/\nGUANABARA: https://www.viajeguanabara.com.br/\nSAMPAIO: https://viacaosampaio.com.br/\n' 
                'PLATAFORMAS: 13, 14, e 15\n\n'
                'TARIFA DE EMBARQUE R$5,25'
            )
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
        elif nome  in cidade_4 and nome  in tarifa_1:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
                'CONTATOS:\n\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\nCENTER TOUR: (32) 3025-3936\n' 
                'SITE: https://www.viacaoprogresso.com.br\nFUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\n' 
                'PLATAFORMAS: 25 e 26\n\n' 
                'TARIFA DE EMBARQUE R$0,85'
			)
        elif nome  in cidade_4 and nome  in tarifa_2:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
                'CONTATOS:\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\n' 
                'CENTER TOUR: (32) 3025-3936\nSITE: https://www.viacaoprogresso.com.br\n' 
                'FUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\nPLATAFORMAS: 25 e 26\n\n'
                'TARIFA DE EMBARQUE R$1,45'
			)
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
        elif nome  in cidade_4 and nome  in tarifa_4:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30 =-=-=-\n\n' 
				'CONTATOS:\nRODOVIÁRIA TRÊS RIOS (24)2251-5050\nPANTUR/JUIZ DE FORA:(32) 3216-2975 - WHATSAPP (32)98849-0016\n' 
				'CENTER TOUR: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h45 / dom 06h - 21h\n' 
				'PLATAFORMAS: 25 e 26\n\n' 
				'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome  in cidade_5 and nome  in tarifa_1:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n' 
                'CONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n'  
                'FUNCIONAMENTO:\nseg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
                'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$0,85'
			)
        elif nome  in cidade_5 and nome  in tarifa_2:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n' 
                'CONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n' 
                'FUNCIONAMENTO:\nseg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
				'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$1,45'
            )
        elif nome  in cidade_5 and nome  in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n' 
				'SITE: https://unidamansur.queropassagem.com.br\n' 
				'FUNCIONAMENTO:\nseg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\ndom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
				'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$2,55')
        elif nome  in cidade_5 and nome  in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n' 
                'CONTATO: (32) 3215-3427\nSITE: https://unidamansur.queropassagem.com.br\n' 
                'FUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n' 
                'PLATAFORMA: 23\n\n'
			    'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome  in cidade_6 and nome  in tarifa_2:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10=-=-=-\n\nCONTATO: (32) 3218-3613\n' 
                'SITE: https://https://www.transur.com.br/horarios_preco\n' 
                'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h\n' 
                'ter à  dom: 06h30- 12h - 13h -19h\n' 
                'PLATAFORMA: 17\n\n' 
                'TARIFA DE EMBARQUE R$1,45'
			)
        elif nome  in cidade_6 and nome  in tarifa_3:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10=-=-=-\n\nCONTATO: (32) 3218-3613\n' 
                'SITE: https://https://www.transur.com.br/horarios_preco\n' 
                'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h - ter à  dom: 06h30- 12h - 13h -19h\n' 
                'PLATAFORMA: 17\n\n' 
                'TARIFA DE EMBARQUE R$2,55'
			)
        elif nome  in cidade_6 and nome  in tarifa_4:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10=-=-=-\n\nCONTATO: (32) 3218-3613\n' 
                'SITE: https://https://www.transur.com.br/horarios_preco\n' 
                'FUNCIONAMENTO: seg: 05h30 - 12h - 13h - 19h\n		ter à  dom: 06h30- 12h - 13h -19h\n' 
                'PLATAFORMA: 17\n\n'
                'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome  in cidade_7 and nome  in tarifa_1:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
                'SITE: https://www.viacaobassamar.queropassagem.com.br\n' 
                'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$0,85'
			)
        elif nome in cidade_7 and nome in tarifa_2:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
                'SITE: https://www.viacaobassamar.queropassagem.com.br\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$1,45'
			)
        elif nome in cidade_7 and nome in tarifa_3:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
				'SITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$2,55'
			)
        elif nome in cidade_7 and nome in tarifa_4:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31 =-=-=-\n\nCONTATO: (32) 3215-1109\n' 
				'SITE: https://www.viacaobassamar.queropassagem.com.br\n'
				'FUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21\n\n'
			    'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_8 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\n' 
				'SITE: http://www.viacaoriodoce.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 07h - 21h\n'
				'PLATAFORMA: 24\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_9 and nome in tarifa_2:
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\n' 
				'SITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMA: 16\n\n'
				'TARIFA DE EMBARQUE R$1,45'
			)
        elif nome in cidade_9 and nome in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\n' 
				'SITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n'
				'PLATAFORMA: 16\n\n'
				'TARIFA DE EMBARQUE R$2,55'
			)
        elif nome in cidade_9 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3025-3936  -  GUICHÊ: 29\n' 
				'SITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n' 
				'PLATAFORMA: 16\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_10 and nome in tarifa_4:
            resultado = (
				'EMPRESA:VIAÇÃO GONTIJO - GUICHÊ: 27\n\nCONTATO:(32) 3215-9458  -  (32) 98710-6414\n' 
				'SITE: https://www.gontijo.com.br/\n\nFUNCIONAMENTO: seg- sex 08h - 20h\nsab - dom - feriados 08h - 12h / 14h - 17h20\n' 
				'PLATAFORMA: 27\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_11 and nome in tarifa_1:
            resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n'
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO: seg à qui: 05h45 - 10h30 - 11h30 às 18h\nsex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n'
				'PLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$0,85'
			)
        elif nome in cidade_11 and nome in tarifa_2:
           	resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n'
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO:\n\nseg à qui: 05h45 - 10h30 - 11h30 às 18h\nsex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n' 
				'PLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$1,45'
			)
        elif nome in cidade_11 and nome in tarifa_3:
            resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n' 
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO:\n\neg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n' 'PLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$2,55'
			)
        elif nome in cidade_11 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n'
				'SITE: https://www.paraibunatransportes.com.br/\n' 
				'FUNCIONAMENTO:\n\nseg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\nsab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_12 and nome in tarifa_4:
           resultado = (
				'EMPRESA: VIAÇÃO EXPRESSO UNIÃO / PLUMA - GUICHÊ: 25\n\nCONTATO: (32) 98710-6414\n' 
				'SITE: https://www.expressouniao.com.br\n\nFUNCIONAMENTO:\n	seg - sex 09h - 18h\nsab dom feriados 14h - 18h (Intervalo: 12h30 - 13h30)\n' 
				'PLATAFORMA: 29\n\n'
				'TARIFA DE EMBARQUE R$5,25'
		   )
        elif nome in cidade_13 and nome in tarifa_3:
            resultado = (
				'=-=-=- EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14 =-=-=-\n\nCONTATOS:\nCentral: (24)2244-1642 ou (24)2244-1600 (GARAGEM)\nPANTUR: 3216-2975\n' 
				'SITE: http://www.unicafacil.com.br/\nFUNCIONAMENTO: seg à sab: 05h40 - 18h30 dom: 05h40 à 17h40\nPLATAFORMA:19\n\n'
				'TARIFA DE EMBARQUE R$2,55')
        elif nome in cidade_13 and nome in tarifa_4:
           resultado = (
			   '=-=-=- EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14 =-=-=-\n\nCONTATOS:\nCentral: (24)2244-1642 ou (24)2244-1600 (GARAGEM)\nPANTUR: 3216-2975\n' 
				'SITE: http://www.unicafacil.com.br/\nFUNCIONAMENTO: seg à sab: 05h40 - 18h30 dom: 05h40 à 17h40\nPLATAFORMA:19\n\n'
			   'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_14 and nome in tarifa_1:
            resultado = (
				'-=- EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07 -=-\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n' 
				'SITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n'
				'PLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO\n\n'
				'TARIFA DE EMBARQUE R$0,85'
			)
        elif nome in cidade_14 and nome in tarifa_2:
            resultado = (
				'-=- EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07 -=-\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n' 
				'SITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n' 
				'PLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO\n\n'
				'TARIFA DE EMBARQUE R$1,45'
			)
        elif nome in cidade_14 and nome in tarifa_3:
            resultado = (
				'-=- EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07 -=-\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n' 
				'SITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n' 
				'PLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO\n\n'
				'TARIFA DE EMBARQUE R$2,55'
		)
        elif nome in cidade_15 and nome in tarifa_4:
            resultado = (
				'EMPRESA: VIAÇÃO ÀGUIA BRANCA - GUICHÊ 26\n\nCONTATO:(32) 98710-6414\nSITE: https://www.aguiabranca.com.br\n' 
				'FUNCIONAMENTO:seg - sex 09h - 18h\nsab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 12\n\n'
				'TARIFA DE EMBARQUE R$5,25'
			)
        elif nome in cidade_16:
            resultado = (
				'EMPRESA: VIAÇÃO ITAPEMIRIM / KAISSARA - GUICHÊ: 29\n\nCONTATOS: (32) 3215-5020 \n0800 723 2121\n' 
				'FUNCIONAMENTO: seg - sab 06h - 19h\ndom 07h - 22h\n\nPLATAFORMA: 28\n\n'
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
        elif nome == 'util' or nome == 'brisa' or nome == 'guanabara' or nome == 'sampaio' or nome == 'gypsyy':
            resultado = (
				'EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY / GUANABARA\n\nGUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830 - WHATSAPP:(32)98833-5497\n\nSITE:\n' 
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
        elif nome == 'progresso' or nome == 'viação progresso' or nome == 'viaçao progresso' or nome == 'viacao progresso':
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
        elif nome == 'gontijo':
            resultado = (
				'EMPRESA:	VIAÇÃO GONTIJO - GUICHÊ: 27\n\nCONTATO:\n(32) 3215-9458\n(32)98710-6414\nSITE: https://www.gontijo.com.br/\n' 
				'FUNCIONAMENTO:\n	seg- sab 08h - 20h20\n	dom - feriados 08h - 12h / 14h - 17h20\n\nPLATAFORMA: 27'
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
				'EMPRESA: VIAÇÃO EXPRESSO UNIÃO / PLUMA - GUICHÊ: 25\n\nCONTATO: (32) 99177-0200\n\nSITE: https://www.expressouniao.com.br\n' 
				'FUNCIONAMENTO:\nseg - sex 09h - 18h\nsab dom feriados 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 29'
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
		# VIAÇÃO ÀGUIA BRANCA ou RODE ROTAS...
		#
        elif nome == 'águia branca' or nome == 'aguia branca' or nome == 'aguiabranca' or nome == 'RODE ROTAS' or nome == 'RODEROTAS' or nome == 'rode rotas' or nome == 'roderotas':
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
