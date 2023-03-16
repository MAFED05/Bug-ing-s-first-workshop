lang = input("Escribe un país de América en minúsculas para saber su Capital: ")
match lang:
    case "canada":
      print("La capital de Canada es Otawwa")
    case "estados unidos":
      print("La capital de Estados Unidos es Washington DC.")
    case "mexico":
      print("La capital de Mexico es México DF.")
    case "belice":
      print("La capital de Belice es Belmopán.")
    case "costa rica":
      print("La capital de Costa Rica es San José.")
    case "el salvador":
      print("La capital de El Salvador es San Salvador.")
    case "guatemala":
      print("La capital de Guatemala es Ciudad de Guatemala.")
    case "honduras":
      print("La capital de Honduras es Tegucigalpa.")
    case "nicaragua":
      print("La capital de Nicaragua es Managua.")
    case "panama":
      print("La capital de de Panama es Panamá.")
    case "argentina":
      print("La capital de Argentina es Buenos Aires.")
    case "bolivia":
      print("La capital de Bolivia es Sucre. Aunque siempre creíste que la capital de Bolivia era La Paz, esta es solo su sede de gobierno, su constitución establece que es Sucre.")
    case "brasil":
      print("La capital de Brasil es Brasilia.")
    case "chile":
      print("La capital de Chile es Santiago de Chile.")
    case "colombia":
      print("La capital de Colombia es Bogotá.")
    case "ecuador":
      print("La capital de Ecuador es Quito.")
    case "paraguay":
      print("La capital de Paraguay es Asunción.")
    case "peru":
      print("La capital de Peru es Lima.")
    case "surinam":
      print("La capital de Surinam es Parabarimo.")
    case "trinidad y tobago":
      print("La capital de Trinidad y Tobago es Puerto España.")
    case "uruguay":
      print("La capital de Uruguay es montevideo.")
    case "venezuela":
      print("La capital de Venezuela es Caracas.")
    case "puerto rico":
      print("Puerto Rico no es considerado un país, ya que pertenece a Estados Unidos.")
    case "antigua y barbuda":
      print("La capital de Antigua y Barbuda es Saint John.")
    case "bahamas":
      print("La capital de Bahamas es Nasáu.")
    case "barbados":
      print("La capital de Barbados es Bridgetown.")
    case "cuba":
      print("La capital de Cuba es La Habana.")
    case "dominica":
      print("La capital de Dominica es Roseau.")
    case "granada":
      print("La capital de Granada es Saint George.")
    case "guyana":
      print("La capital de Guyana es Georgetown.")
    case "haiti":
      print("La capital de Haití es Puerto Príncipe.")
    case "jamaica":
      print("La capital de Jamaica es Kingston.")
    case "republica dominicana":
      print("La capital de República Dominicana es Santo Domingo.")
    case "san cristobal y nieves":
      print("La capital de San Cristóbal y Nieves es Basseterre.")
    case "san vicente y las granadinas":
      print("La capital de San Vicente y las Granadinas es Kingstown.")
    case "santa lucia":
      print("La capital de Santa Lucía es Castries.")
    case "alaska":
      print("Alaska pertenece a uno de los 50 estados que conforman Estados Unidos, no es un país.")
    case "groenlandia":
      print("Groenlandia forma parte de Dinamarca")
    case _:
      print("País no identificado.")