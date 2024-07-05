import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from folium.plugins import Draw

# Função para exibir o mapa
def Mapa():   
    st.header('Ultrapassagem de Demanda', divider='red')  
    # Cria o mapa centralizado em uma localização específica
    m = folium.Map(location=(-3.71839, -38.5434))
    Draw(export=True).add_to(m)

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
 
    # Exibe o mapa no Streamlit
    st_folium(m, width=725, height=500)

    st.write('Desenvolvido por Otavio Viana')

# Função para a página faotr
def Fator():
     
    from streamlit_folium import st_folium  

    st.header('Fator de Potência', divider='red')  

    # Cria o mapa centralizado em uma localização específica
    m = folium.Map(location=(-3.71839, -38.5434))

    # Cria grupos de marcadores
    grupo1 = folium.FeatureGroup(name='UN-BAJ') # cor red
    grupo2 = folium.FeatureGroup(name='UN-BBA') # cor blue
    grupo3 = folium.FeatureGroup(name='UN-BBJ') # cor green
    grupo4 = folium.FeatureGroup(name='UN-BCL') # cor yellow
    grupo5 = folium.FeatureGroup(name='UN-BML') # cor yellow
    grupo6 = folium.FeatureGroup(name='UN-BMO') # cor orange
    grupo7 = folium.FeatureGroup(name='UN-BSA') # cor gray
    grupo8 = folium.FeatureGroup(name='UN-BSC') # cor gold

    # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-7.215325119082865, -40.137157512804485],
        tooltip="9001739",
        popup='''
            CSB-04 + CSB-05 DO SI ALAGOINHA
            FP MÉDIO: 0,8672
            KWH MÉDIO: 242
            KWAR MÉDIO: 138,96
            NOVO FP: 0,88
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)

    # Adiciona mais marcadores ao grupo 2 (exemplo)
    folium.Marker(
        location=[-6.177118705578564, -39.90227596281519],
        tooltip="9003497",
        popup='''
            CSB-04 + CSB-05 + CSB-06 + SSD-04 
            FP MÉDIO: 0,7184
            KWH MÉDIO: 68
            KWAR MÉDIO: 65,84
            NOVO FP: 0,76
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)

   
    folium.Marker(
        location=[-7.215325119082869, -40.137157512804489],
        tooltip="9005483",
        popup='''
            ETA ALAGOINHA DO SI ALAGOINHA
            FP MÉDIO: 0,8548
            KWH MÉDIO: 62
            KWAR MÉDIO: 37,64
            NOVO FP: 0,9
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)
      # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-6.263369, -39.927577],
        tooltip="9003496 ",
        popup='''
            ETA-02 - SÃO GONÇALO DO SI CATARINA
            FP MÉDIO: 0,6404
            KWH MÉDIO: 52
            KWAR MÉDIO: 62,36
            NOVO FP: 0,69
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)  

    folium.Marker(
        location=[-3.799705819726937, -40.2562182867667],
        tooltip="9011109",
        popup='''
            CS-02 + ETA-02 DO SAA ARNEIROZ
            FP MÉDIO: 0,7592
            KWH MÉDIO: 20
            KWAR MÉDIO: 17,15
            NOVO FP: 0,9
            ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)  # Adiciona marcadores ao grupo 1


    folium.Marker(
        location=[-4.971008733234479, -39.014706746646276],
        tooltip="1389773",
        popup='''
                ETA TAPUIARÁ (SISAR)
                FP MÉDIO: 0,9
                KWH MÉDIO: 46
                KWAR MÉDIO: 22,28
                NOVO FP: 0,95
                ''',
        icon=folium.Icon(icon="info-sign", color='blue')
    ).add_to(grupo2)  # Adiciona marcadores ao grupo 1

    folium.Marker(
        location=[-4.971008733234, -39.014706746646],
        tooltip="9006255",
        popup='''
                ETE HERVAL DO SES QUIXADÁ (ETE 
                FP MÉDIO: 0,94
                KWH MÉDIO: 47
                KWAR MÉDIO: 17,06
                NOVO FP: 0,98
                ''',
        icon=folium.Icon(icon="info-sign", color='blue')
    ).add_to(grupo2) 

    folium.Marker(
        location=[-5.101684, -38.907127],
        tooltip="9006487",
         popup='''
                ETE HERVAL DO SES QUIXADÁ (ETE 
                FP MÉDIO: 0,9632
                KWH MÉDIO: 333
                KWAR MÉDIO: 92,93
                NOVO FP: 0,97
                ''',
        icon=folium.Icon(icon="info-sign", color='blue')
    ).add_to(grupo2) 

    folium.Marker(
        location=[-4.572949281328842, -37.73086020763538],
        tooltip="57326141",
         popup='''
                EEAB ALTO DA CHEIA 
                FP MÉDIO: 0,5892
                KWH MÉDIO: 35
                KWAR MÉDIO: 48,00
                NOVO FP: 0,65
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  
    
    folium.Marker(
        location=[-4.970218235400555, -37.97638711534415],
        tooltip="9001789",
        popup='''
                CS-01 + CSB-01 DO SAA RUSSAS 
                FP MÉDIO: 0,8852
                KWH MÉDIO: 241
                KWAR MÉDIO: 126,66
                NOVO FP: 0,9
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  
    
    folium.Marker(
        location=[-4.856106, -37.776537],
        tooltip="9003155",
        popup='''
                CS-01 DO SI JAGUARUANA
                FP MÉDIO: 0,8256
                KWH MÉDIO: 35
                KWAR MÉDIO: 23,92
                NOVO FP: 0,9
                ''',
        icon=folium.Icon(icon="info-sign", color='green')
    ).add_to(grupo3)  

    folium.Marker(
        location=[-4.184165379772898, -38.09278727953362],
        tooltip="9010726",
        popup='''
                CS-01 + CSB-01 DO SI BEBERIBE
                FP MÉDIO: 0,8164
                KWH MÉDIO: 42
                KWAR MÉDIO: 29,71
                NOVO FP: 0,88
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo5)  # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-4.126311530623035, -38.2396788246681],
        tooltip="9000805",
        popup='''
                ETA-01 - CASCAVEL DO SAA CASCAVEL
                FP MÉDIO: 0,772
                KWH MÉDIO: 68
                KWAR MÉDIO: 55,99
                NOVO FP: 0,81
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo5)  
    
    folium.Marker(
        location=[-3.7997058197269378, -40.25621828676672],
        tooltip="9010758",
        popup='''
                EEE-01 - ALAMEDA DAS PALMEIRAS
                FP MÉDIO: 0,6084
                KWH MÉDIO: 18
                KWAR MÉDIO: 23,48
                NOVO FP: 0,75
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo5)  
    
    folium.Marker(
        location=[-3.7997058197269378, -40.25621828676672],
        tooltip="9006457",
        popup='''
                ETA-02 - RIVIERA DO SAA TAPERA
                FP MÉDIO: 0,6952
                KWH MÉDIO: 105
                KWAR MÉDIO: 108,57
                NOVO FP: 0,81
                ''',
        icon=folium.Icon(icon="info-sign", color='red')
    ).add_to(grupo1)  # Adiciona marcadores ao grupo 1
    folium.Marker(
        location=[-3.909335, -38.379695],
        tooltip="9001053",
        popup='''
                ETA AQUIRAZ DO SI AQUIRAZ
                FP MÉDIO: 0,5852
                KWH MÉDIO: 84
                KWAR MÉDIO: 116,40
                NOVO FP: 0,61
                ''',
        icon=folium.Icon(icon="info-sign", color='yellow')
    ).add_to(grupo5)  # Adiciona marcadores ao grupo 1
    
    
    folium.Marker(
        location=[-4.343936, -38.864567],
        tooltip="9004978",
        popup='''
                EEAT-02 DO SAA BATURITÉ
                FP MÉDIO: 0,4276
                KWH MÉDIO: 101
                KWAR MÉDIO: 213,52
                NOVO FP: 0,44
                ''',
        icon=folium.Icon(icon="info-sign", color='orange')
    ).add_to(grupo6)  # Adiciona marcadores ao grupo 1
    
    folium.Marker(
        location=[-7.253806, -39.144806],
        tooltip="264104",
        popup='''
                ETA MISSÃO VELHA DO SAA MISSÃO 
                FP MÉDIO: 0,5104
                KWH MÉDIO: 87
                KWAR MÉDIO: 146,58
                NOVO FP: 0,53
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1
    
    folium.Marker(
        location=[-6.645809134125352, -38.70013511748416],
        tooltip="9009648",
        popup='''
                ETA BAIXIO DO SI BAIXIO
                FP MÉDIO: 0,6772
                KWH MÉDIO: 52
                KWAR MÉDIO: 56,50
                NOVO FP: 0,73
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1
    
    folium.Marker(
        location=[-3.7997058197269378, -40.25621828676672],
        tooltip="9001778",
        popup='''
                ETA BAIXIO DO SI BAIXIO
                FP MÉDIO: 0,4812
                KWH MÉDIO: 6
                KWAR MÉDIO: 10,93
                NOVO FP: 0,87
                ''',
        icon=folium.Icon(icon="info-sign", color='gray')
    ).add_to(grupo7)  # Adiciona marcadores ao grupo 1
    



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
    st.write('Desenvolvido por Otavio Viana')
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
if selected == "Mapa":
    Mapa()
elif selected == "Fator":
    Fator()

# Run the app
if __name__ == "__main__":
    pass
