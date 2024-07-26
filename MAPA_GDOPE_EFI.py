import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
import datetime

# Data - copia na busca, um dia anterior ao executado aqui só é valido para diário
hoje = datetime.datetime.now()
ontem = hoje - datetime.timedelta(days=1)
dia_exec = ontem.strftime('%d/%m/%Y')


icon_base64 = "https://img.icons8.com/?size=100&id=9267&format=png&color=8A8A11"  

st.set_page_config(
    page_icon=icon_base64,
    layout="centered",  
    initial_sidebar_state="auto" 
)

# Função para exibir o mapa
def Mapa():   
    from folium.plugins import Draw
    st.header('Ultrapassagem de Demanda', divider='red')  
    # Cria o mapa centralizado em uma localização específica
    m = folium.Map(location=(-3.71839, -38.5434))
    
    #! ULTRAPASSADOS
    
    folium.Marker(
        location=[-7.253806, -39.144806],
        tooltip="264104",
        popup="ETA MISSÃO VELHA DO SAA MISSÃO",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.971008733234479, -39.014706746646276],
        tooltip="1389773",
        popup="ETA TAPUIARÁ (SISAR)",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    # Adiciona marcadores ao mapa
    folium.Marker(
        location=[-3.7997058197269378, -40.25621828676672],
        tooltip="1017401",
        popup="ETA - FORQUILHA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

# Adiciona marcadores ao mapa
    folium.Marker(
        location=[-4.227706750853777, -39.191005690499146],
        tooltip="1725904",
        popup="CS-01 + ETA CARIDADE DO SAA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-5.463787529458468, -40.78005110289483],
        tooltip="9009221",
        popup="ETA - NOVO ORIENTE",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-3.829556919772068, -38.557312423271],
        tooltip="9003917",
        popup="SEDE ADMINISTRATIVA DA UNMTS",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)


    folium.Marker(
        location=[-5.740362527782114, -39.626396523291234],
        tooltip="1572902",
        popup="ETA MOMBAÇA / PA-01 / PA-02",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-3.7955546205116084, -39.273129129888524],
        tooltip="433212",
        popup="CS-01 + ETA PENTECOSTE DO SAA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.959836232923555, -39.025312987593374],
        tooltip="9000668",
        popup="EEAT-02 + EEAT-05 DO SAA QUIXADÁ ",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-6.7272835029943625, -38.715568213490656],
        tooltip="9009457",
        popup="SSD-01 DO SI BAIXIO",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.970218235400555, -37.97638711534415],
        tooltip="9001789",
        popup="CS-01 + CSB-01 DO SAA RUSSAS",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.49034751474691, -38.5963726386168],
        tooltip="9011318",
        popup="CS-02 + EEAB-02 DO SI OCARA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.694321662853855, -38.039499553026694],
        tooltip="9006300",
        popup="EEAB-02 DO SAA PALHANO",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.031224815604646, -38.92421612570589],
        tooltip="9008099",
        popup="EEAT-02 DO SI ITAPEBUSSU",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-7.253169033126221, -39.33619264519125],
        tooltip="57655138",
        popup="RUA JACOBINA DE SOUZA 0 - ETA - FREI",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.369645314876368, -38.81055782304524],
        tooltip="9001831",
        popup="EEAT-02 DO SI ARACOIABA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-5.613291822298348, -38.76342058218057],
        tooltip="52392974",
        popup="CS-02 DO SAA JAGUARETAMA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-7.23022923908172, -39.32172410613558],
        tooltip="9011153",
        popup="CSB-44 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-7.09155079456411, -40.02843112304951],
        tooltip="9001452",
        popup="CS-01 + ETA POTENGI DO SAA POTENGI",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-4.178427290708941, -38.86420648158024],
        tooltip="430035",
        popup="CSB-15 + CSB-19 + ETA PACOTI DO SAA",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-6.0467231585912975, -38.46026353035573],
        tooltip="9007210",
        popup="ETA PEREIRO DO SAA PEREIRO",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-7.24121298878452, -39.27958192822686],
        tooltip="57654978",
        popup="SSD-38 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-7.24088868219311, -39.31288428548631],
        tooltip="9004223",
        popup="CSB-08 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(m)

    folium.Marker(
        location=[-3.035822476465559, -41.240443822766395],
        tooltip="9001931",
        popup="CS-01 + ETA CHAVAL",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    # SEM TELEMETRIA

    folium.Marker(
        location=[-7.8299449952584625, -39.066130760625356],
        tooltip="9001614",
        popup="SSD-01 DO SAA PENAFORTE",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-3.538486546727683, -40.45857005867043],
        tooltip="9011108",
        popup="CS-03 (AÇUDE JENIPAPO) - MERUOCA",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-5.194720954121337, -40.65741171036],
        tooltip="1525146",
        popup="CS-01 (BARRAGEM DO RIO POTY) - CRATEÚS",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-6.98231141217335, -39.715949316061],
        tooltip="1814261",
        popup="EEAB-01 / RAP-01 (ALTANEIRA)",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-5.271106076454046, -40.66838884132236],
        tooltip="24444213",
        popup="CS-02 (EECS-02B - AÇUDE ",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-6.177118705578564, -39.90227596281519],
        tooltip="9003497",
        popup="CSB-04 + CSB-05 + CSB-06 + SSD-04",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-5.8920078717565785, -38.62193137103304],
        tooltip="40757962",
        popup="EEAB-03 (AQUINÓPOLIS - JAGUARIBE)",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-4.451999689328035, -38.15944470734253],
        tooltip="32649938",
        popup="CS-01 + CSB-01 + ETA SERRA DO FÉLIX ",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-3.663010386498672, -40.483970195019644],
        tooltip="1780598",
        popup="CS-01 + EEAB-01 (RIO COREAÚ)",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    folium.Marker(
        location=[-7.208721840829631, -39.31576754288003],
        tooltip="671944",
        popup="CSB-06 DO SAA JUAZEIRO DO NORTE",
        icon=folium.Icon(icon="lock", color='gray')
    ).add_to(m)

    #* OK

    folium.Marker(
        location=[-5.2127108233333175, -38.13521869754026],
        tooltip="1053122",
        popup="CS-01 + ETA TABULEIRO DO NORTE",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-3.896925321562796, -38.650295228769664],
        tooltip="672007",
        popup="PT-02 / MED-02 (BARBALHA)",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-3.733014021487103, -38.48611194297341],
        tooltip="52701355",
        popup="P-14 (IPPO)",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-5.099758471122712, -40.13826565742101],
        tooltip="9001409",
        popup="CSB-03 + CSB-08 + CSB-09 + ETA IPU",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-3.718116434453405, -38.5301484259314],
        tooltip="9001586",
        popup="ESTAÇÃO DE RECALQUE REUNI (SCA - AQUI)",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-3.7428131240486155, -38.47521279767017],
        tooltip="9001407",
        popup="UNIDADE RESERVAÇÃO CAIÇARA",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-5.083748176076057, -40.6843323420246],
        tooltip="9001388",
        popup="CS-02 + ETA CRATEÚS",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-3.7811121187044445, -38.53884798959521],
        tooltip="201702",
        popup="P-23 / UA-23 (TAMARINEIRA)",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-5.199632526095081, -40.66694675453755],
        tooltip="9001530",
        popup="CS-01 + ETA NOVO ORIENTE",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.Marker(
        location=[-4.967820563930663, -37.97774306412788],
        tooltip="9001846",
        popup="CSB-01 + CSB-03 + CSB-04 + EEAB-03 ",
        icon=folium.Icon(icon="user", color='green')
    ).add_to(m)

    folium.plugins.Fullscreen(
        position="topright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(m) 
    Draw(export=True).add_to(m)
    st_folium(m, width=725, height=500)
    st.write(f'Referência {dia_exec}')
    st.write('Gerência de Controle, Desenvolvimento e Eficiência Operacional')

# Função para a página faotr
def Fator():
    
    from folium.plugins import Draw
    from streamlit_folium import st_folium  

    st.header('Fator de Potência', divider='red')  

    # Cria o mapa centralizado em uma localização específica
    m = folium.Map(location=(-3.71839, -38.5434))

    # Cria grupos de marcadores
    grupo1 = folium.FeatureGroup(name='UN-BAJ') # cor red
    grupo2 = folium.FeatureGroup(name='UN-BBA') # cor blue
    grupo3 = folium.FeatureGroup(name='UN-BBJ') # cor green
    grupo4 = folium.FeatureGroup(name='UN-BCL') # cor yellow
    grupo5 = folium.FeatureGroup(name='UN-BML') # cor darkpurple
    grupo6 = folium.FeatureGroup(name='UN-BMO') # cor orange
    grupo7 = folium.FeatureGroup(name='UN-BSA') # cor gray
    grupo8 = folium.FeatureGroup(name='UN-BSC') # cor black



    # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-7.686378305787442, -39.005251775875315],
        tooltip="9003389",
        popup='''
            CSB-04 + CSB-05 + CSB-06 DO SAA JATI
            FP MÉDIO: 0,8316
            KWH MÉDIO: 27
            KWAR MÉDIO: 18,03
            NOVO FP: 0,93
            ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)

    # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-7.215325119082865, -40.137157512804485],
        tooltip="9001739",
        popup='''
            CSB-04 + CSB-05 DO SI ALAGOINHA
            FP MÉDIO:0,8668
            KWH MÉDIO: 242
            KWAR MÉDIO: 139,22
            NOVO FP: 0,88
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)
    

    # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-4.743882676481315, -40.9233633540918],
        tooltip="1725914",
        popup='''
            SSD-01 DO SAA PORANGA
            FP MÉDIO: 0,554
            KWH MÉDIO: 112
            KWAR MÉDIO: 
            NOVO FP: 1
            ''',
        icon=folium.Icon(icon="info-sign", color='black')
    ).add_to(grupo8)

    # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-5.281617695288665, -40.67139076056312],
        tooltip="24444213",
        popup='''
            CS-02 (EECS-02B) DO SAA CRATEÚS
            FP MÉDIO: 0,92
            KWH MÉDIO: 112
            KWAR MÉDIO: 47,71
            NOVO FP: 0,94
            ''',
        icon=folium.Icon(icon="info-sign", color='black')
    ).add_to(grupo8)
        # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-5.167986142490234, -40.66653494456778],
        tooltip="9003914",
        popup='''
            SEDE ADM. DA UNBSC + ETE 
            FP MÉDIO: 0,92
            KWH MÉDIO: 44   
            KWAR MÉDIO: 3,22
            NOVO FP: 1
            ''',
        icon=folium.Icon(icon="info-sign", color='black')
    ).add_to(grupo8)


    # Adiciona mais marcadores ao grupo 2 (exemplo)
    folium.Marker(
        location=[-6.177118705578564, -39.90227596281519],
        tooltip="9003497",
        popup='''
            CSB-04 + CSB-05 + CSB-06 + SSD-04 
            FP MÉDIO: 0,6308
            KWH MÉDIO: 68
            KWAR MÉDIO: 83,65
            NOVO FP: 0,67
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)

   
    folium.Marker(
        location=[-7.215325119082869, -40.137157512804489],
        tooltip="9005483",
        popup='''
            ETA ALAGOINHA DO SI ALAGOINHA
            FP MÉDIO: 0,9792
            KWH MÉDIO: 63
            KWAR MÉDIO: 13,05
            NOVO FP: 1
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)
      # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-6.263369, -39.927577],
        tooltip="9003496 ",
        popup='''
            ETA-02 - SÃO GONÇALO DO SI CATARINA
            FP MÉDIO: 0,6692
            KWH MÉDIO: 57
            KWAR MÉDIO: 63,29
            NOVO FP: 0,71
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)  

    folium.Marker(
        location=[-3.799705819726937, -40.2562182867667],
        tooltip="9011109",
        popup='''
            CS-02 + ETA-02 DO SAA ARNEIROZ
            FP MÉDIO: 0,6604
            KWH MÉDIO: 22
            KWAR MÉDIO: 25,02
            NOVO FP: 0,78
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)  # Adiciona marcadores ao grupo 1


    folium.Marker(
        location=[-4.971008733234479, -39.014706746646276],
        tooltip="1389773",
        popup='''
                ETA TAPUIARÁ (SISAR)
                FP MÉDIO: 0,8892
                KWH MÉDIO: 48
                KWAR MÉDIO: 24,70
                NOVO FP: 0,94
                ''',
        icon=folium.Icon(icon="info-sign", color='blue')
    ).add_to(grupo2)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-4.971008733234, -39.014706746646],
        tooltip="9006255",
        popup='''
                ETE HERVAL DO SES QUIXADÁ (ETE 
                FP MÉDIO: 0,9428
                KWH MÉDIO: 48
                KWAR MÉDIO: 16,97
                NOVO FP: 0,98
                ''',
        icon=folium.Icon(icon="info-sign", color='blue')
    ).add_to(grupo2) 

    folium.Marker(
        location=[-5.101684, -38.907127],
        tooltip="9006487",
         popup='''
                ETE HERVAL DO SES QUIXADÁ (ETE 
                FP MÉDIO: 0,9224
                KWH MÉDIO: 334
                KWAR MÉDIO: 139,86
                NOVO FP: 0,93
                ''',
        icon=folium.Icon(icon="info-sign", color='blue')
    ).add_to(grupo2) 

    folium.Marker(
        location=[-4.572949281328842, -37.73086020763538],
        tooltip="57326141",
         popup='''
                EEAB ALTO DA CHEIA 
                FP MÉDIO: 0,984
                KWH MÉDIO: 36
                KWAR MÉDIO: 6,52
                NOVO FP: 1
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  
    
    folium.Marker(
        location=[-4.970218235400555, -37.97638711534415],
        tooltip="9001789",
        popup='''
                CS-01 + CSB-01 DO SAA RUSSAS 
                FP MÉDIO: 0,96
                KWH MÉDIO: 244
                KWAR MÉDIO: 71,17
                NOVO FP: 0,97
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  
    
    folium.Marker(
        location=[-4.856106, -37.776537],
        tooltip="9003155",
        popup='''
                CS-01 DO SI JAGUARUANA
                FP MÉDIO: 0,834
                KWH MÉDIO: 36
                KWAR MÉDIO: 23,82
                NOVO FP: 0,91
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  

    folium.Marker(
        location=[-4.184165379772898, -38.09278727953362],
        tooltip="9010726",
        popup='''
                CS-01 + CSB-01 DO SI BEBERIBE
                FP MÉDIO: 0,828
                KWH MÉDIO: 42
                KWAR MÉDIO: 28,44
                NOVO FP: 0,89
                ''',
        icon=folium.Icon(icon="info-sign", color='darkpurple')
    ).add_to(grupo5)  # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-4.126311530623035, -38.2396788246681],
        tooltip="9000805",
        popup='''
                ETA-01 - CASCAVEL DO SAA CASCAVEL
                FP MÉDIO: 0,766
                KWH MÉDIO: 68
                KWAR MÉDIO: 57,07
                NOVO FP: 0,81   
                ''',
        icon=folium.Icon(icon="info-sign", color='darkpurple')
    ).add_to(grupo5)  
    
    folium.Marker(
        location=[-3.865320742942022, -38.51957248898521],
        tooltip="9010758",
        popup='''
                EEE-01 - ALAMEDA DAS PALMEIRAS
                FP MÉDIO: 0,574
                KWH MÉDIO: 18
                KWAR MÉDIO: 25,68
                NOVO FP: 0,7
                ''',
        icon=folium.Icon(icon="info-sign", color='darkpurple')
    ).add_to(grupo5)  
    
    folium.Marker(
        location=[-3.923759296531435, -38.32913481639625],
        tooltip="9006457",
        popup='''
                ETA-02 - RIVIERA DO SAA TAPERA
                FP MÉDIO: 0,3488
                KWH MÉDIO: 108
                KWAR MÉDIO: 290,19
                NOVO FP: 0,36
                ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo5)  # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-3.909335, -38.379695],
        tooltip="9001053",
        popup='''
                ETA AQUIRAZ DO SI AQUIRAZ
                FP MÉDIO: -0,09
                KWH MÉDIO: 84
                KWAR MÉDIO: -929,55
                NOVO FP: 0,09 
                ''',
        icon=folium.Icon(icon="info-sign", color='darkpurple')
    ).add_to(grupo5)  # Adiciona marcadores ao grupo 1
    
    
    folium.Marker(
        location=[-4.343936, -38.864567],
        tooltip="9004978",
        popup='''
                EEAT-02 DO SAA BATURITÉ
                FP MÉDIO: 0,4688
                KWH MÉDIO: 101
                KWAR MÉDIO: 190,30
                NOVO FP: 0,48
                ''',
        icon=folium.Icon(icon="info-sign", color='orange')
    ).add_to(grupo6)  # Adiciona marcadores ao grupo 1
    
    folium.Marker(
        location=[-7.253806, -39.144806],
        tooltip="264104",
        popup='''
                ETA MISSÃO VELHA DO SAA MISSÃO 
                FP MÉDIO: 0,4736
                KWH MÉDIO: 87
                KWAR MÉDIO: 161,79
                NOVO FP: 0,49
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1
    
    folium.Marker(
        location=[-6.645809134125352, -38.70013511748416],
        tooltip="9009648",
        popup='''
                ETA BAIXIO DO SI BAIXIO
                FP MÉDIO: 0,0308
                KWH MÉDIO: 54
                KWAR MÉDIO: 1752,41
                NOVO FP: 0,03
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1
    
    folium.Marker(
        location=[-7.084890545877496, -39.67429950342538],
        tooltip="9001778",
        popup='''
                ETA BAIXIO DO SI BAIXIO
                FP MÉDIO: 0,6236
                KWH MÉDIO: 6
                KWAR MÉDIO: 7,52
                NOVO FP: 1
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1


    folium.Marker(
        location=[-5.320200228821421, -40.31889907121499],
        tooltip="9006221",
        popup='''
                CS-01 DO SAA TAMBORIL
                FP MÉDIO: -0,5252
                KWH MÉDIO: 23
                KWAR MÉDIO: -37,27
                NOVO FP: 0,46
                ''',
        icon=folium.Icon(icon="info-sign", color='black')
    ).add_to(grupo8)  # Adiciona marcadores ao grupo 1


    folium.Marker(
        location=[-5.320200228821421, -40.31889907121499],
        tooltip="9009232",
        popup='''
                CSB-16 DO SAA INDEPENDÊNCIA
                FP MÉDIO: 0,9228
                KWH MÉDIO: 50
                KWAR MÉDIO: 20,88
                NOVO FP: 0,97
                ''',
        icon=folium.Icon(icon="info-sign", color='black')
    ).add_to(grupo8)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-6.900540812779592, -39.197704231852825],
        tooltip="9005925",
        popup='''
                SSD-09 DO SAA BARBALHA
                FP MÉDIO: 0,4924
                KWH MÉDIO: 50
                KWAR MÉDIO: 88,38
                NOVO FP: 0,53
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-4.481196007126577, -37.72077819863923],
        tooltip="51353772",
        popup='''
                SSD-08 - SAA C. QUEB + ETE C. QUEB - 
                FP MÉDIO: 0,6968
                KWH MÉDIO: 31
                KWAR MÉDIO: 31,91
                NOVO FP: 0,79
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-3.439917, -39.634094],
        tooltip="879191",
        popup='''
                CS-01 (AÇUDE POÇO VERDE)
                FP MÉDIO: 0,5748
                KWH MÉDIO: 79
                KWAR MÉDIO: 112,47
                NOVO FP: 0,6
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo4)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-7.1727065505002505, -39.30001203312737],
        tooltip="55972149",
        popup='''
                PT-65 / EEAT-22 (LEANDRO BEZERRA I E II - JUAZ. DO NORTE)
                FP MÉDIO: 0,596
                KWH MÉDIO: 31
                KWAR MÉDIO: 41,77
                NOVO FP: 0,67
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-3.195561080054889, -39.267229772554295],
        tooltip="9010231",
        popup='''
                SSD-01 + SSD-02 + SSD-03 + SSD-04
                FP MÉDIO: 0,956
                KWH MÉDIO: 21
                KWAR MÉDIO: 6,44
                NOVO FP: 1
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo4)  # Adiciona marcadores ao grupo 1


    folium.Marker(
        location=[-4.057075862775062, -39.45523355501355],
        tooltip=" 50290416",
        popup='''
                CS-02 DO SAA GENERAL SAMPAIO
                FP MÉDIO: 0,7604
                KWH MÉDIO: 14
                KWAR MÉDIO: 5,98
                NOVO FP: 0,98
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo4)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-4.057075862775062, -39.45523355501355],
        tooltip="44786393",
        popup='''
                CS-02 DO SAA GENERAL SAMPAIO
                FP MÉDIO: 0,774
                KWH MÉDIO: 14
                KWAR MÉDIO: 11,45
                NOVO FP: 0,96
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo4)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-3.4847250042999764, -40.01882742283056],
        tooltip="52207102",
        popup='''
                CS-03 + ETA-02 DO SAA BROTAS
                FP MÉDIO: 0,8624
                KWH MÉDIO: 52
                KWAR MÉDIO: 
                NOVO FP: 1
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo4)  # Adiciona marcadores ao grupo 1

    # Adiciona os grupos ao mapa
    grupo1.add_to(m)
    grupo2.add_to(m)
    grupo3.add_to(m)
    grupo4.add_to(m)
    grupo5.add_to(m)
    grupo6.add_to(m)
    grupo7.add_to(m)
    grupo8.add_to(m)

    # Adiciona o controle de camadas ao mapa
    folium.LayerControl(collapsed=False).add_to(m)

    folium.plugins.Fullscreen(
        position="topright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(m)
    Draw(export=True).add_to(m)
    # Exibe o mapa no Streamlit
    st_folium(m, width=725, height=500)
    st.write(f'Referência {dia_exec}')
    st.write('Gerência de Controle, Desenvolvimento e Eficiência Operacional')
   

    print (2)
# Barra de navegação
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",
        options=["Demanda", "Fator"],
        icons=["map", "map"],
        menu_icon="cast",
        default_index=0,
    )

# Exibe a página selecionada
if selected == "Demanda":
    Mapa()
elif selected == "Fator":
    Fator()

# Run the app
if __name__ == "__main__":
    pass
