import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#usado teste 10
from selenium.webdriver.support.ui import Select

@pytest.fixture
def browser():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://www.phoenix.edu/")
  #maximiza a janela
  driver.maximize_window()
  return driver

# 1 TESTAR CHAT
def test_chat(browser):
  actions = ActionChains(browser) #armazena ações
  chat = browser.find_element_by_xpath("//*[@id='cx_widget_side_bar']/div[1]") #elemento do balao chat
  sleep(1)
  browser.execute_script("arguments[0].click();", chat) #clica no chat
  sleep(1)
  firstname = browser.find_element_by_xpath("//*[@id='cx_webchat_form_firstname']") #pega o input first name
  sleep(1)
  firstname.send_keys("Mario") #preenche Mario
  sleep(1)
  lastname = browser.find_element_by_xpath("//*[@id='cx_webchat_form_lastname']") #last name
  sleep(1)
  lastname.send_keys("Da Silva") #preenche da silva
  sleep(1)
  email = browser.find_element_by_xpath("//*[@id='cx_webchat_form_email']") #email..
  sleep(1)
  email.send_keys("mario@gmail.com") #preenche email
  sleep(1)
  button = browser.find_element_by_xpath("/html/body/div[9]/div/div/div[1]/button[1]") #botao pra minimizar chat
  sleep(1)
  actions.click(button) #clicar no botao pra minimizar chat /fila
  sleep(1)
  actions.perform() #executa toda fila de ações
  sleep(1)
  assert firstname.get_property("value") == "Mario" #verifica se o texto FIRST NAME é MARIO
  sleep(1)

# 2 TESTAR O DIA
def test_tabela(browser):
  actions = ActionChains(browser)
  element = browser.find_element_by_xpath("//*[@id='content_timer']/div/div/div/div[3]/div/div/a") #Botão More Start Dates 
  browser.execute_script("arguments[0].click();", element) #clica no botão
  sleep(4)
  ol = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/section[1]/div/div/div/div/div/div/div[1]/div/ol") #pega toda a lista de tab
  li = ol.find_elements_by_tag_name("li")[1] #pega o segundo elemento do OL, Graduate!
  browser.execute_script("arguments[0].click();", li) #clica no botão
  sleep(2)
  tables = browser.find_elements_by_tag_name("table") #pega a tabela que vai mostrar na tela
  assert li.text == "Graduate" #verifica se a lista é Graduate
  table = tables[2] #pega a terceira tabela Graduate Programs
  caption = table.find_element_by_tag_name("caption") #pega o caption da tabela
  actions.move_to_element(caption) #move a tela "scroll" /fila
  actions.perform() #executa a fila
  sleep(2)
  assert caption.text == "Graduate Programs" #verifica se o caption é Graduate Programs
  background = caption.value_of_css_property("background") #pega o background do caption
  assert background == "rgb(0, 24, 35) none repeat scroll 0% 0% / auto padding-box border-box" #verifica se é igual ao texto
  td = table.find_element_by_tag_name("td") #pega o primeiro td "primeira célula da tabela"
  assert td.text == "August 25, 2021" #verifica se é 25 de agosto

# 3 TESTA O TOTAL DE TABELAS
def test_mais_detalhes(browser):
  element = browser.find_element_by_xpath("//*[@id='content_timer']/div/div/div/div[3]/div/div/a") #botao MORE START DATES
  browser.execute_script("arguments[0].click();", element) #clica nesse botao..
  sleep(1) #dorme
  tables = browser.find_elements_by_tag_name("table") #pega todas tabelas, 4 no total
  sleep(1)
  Var = len(tables) #pega o total de tabelas
  sleep(1)
  assert Var > 2 #verifica se é maior que 2 "4>2"
  table = tables[0] #pega a primeira tabela
  caption = table.find_element_by_tag_name("caption") #pega o caption da primeira tabela
  assert caption.text == "Associate and Bachelor's*" #verifica o título da tabela
  background = caption.value_of_css_property("background") #pega o background "obtido pelo print"
  assert background == "rgb(0, 24, 35) none repeat scroll 0% 0% / auto padding-box border-box" #faz o teste

# 4 TESTA SE EXISTE O BOTAO FIND YOUR PROGRAM NO MEGAMENU
def test_menu(browser):
  degree_program = browser.find_element_by_xpath('//*[@id="degree"]') #botao DEGREE'S & PROGRAMS pra abrir o MEGA MENU
  actions = ActionChains(browser) #cria uma fila de ações
  sleep(2)
  actions.click(degree_program) #clica no botao Degree_Program /fila
  actions.perform() #executa a fila
  find_your_program = browser.find_element_by_xpath('//*[@id="btnTemplate_264"]/a') #botao FIND YOUR PROGRAM
  sleep(2)
  assert find_your_program.text == "Find your Program" #verifica se o texto é FIND YOUR PROGRAM 

# 5 TESTA SE O ALT DA IMAGEM DO MAJOR é JohnLEstrada_SmallSize_reducedNoise
def test_image(browser):
  admissions = browser.find_element_by_xpath('//*[@id="main-menu"]/li[4]/a') #botao Admissions
  actions = ActionChains(browser) #cria a fila de ações
  actions.click(admissions) #clica no botão /fila
  actions.perform() #executa a fila
  sleep(3) #dormir 3 segundos
  veterans = browser.find_element_by_xpath('//*[@id="undefined_Admissions_9"]') #pega o botão Veteran
  actions = ActionChains(browser) #cria a fila de ações
  actions.click(veterans) #clica no Botao Vetaran /fila
  actions.perform() #executa a fila 
  sleep(3)
  veteran_image = browser.find_element_by_xpath('//*[@id="cq-image-jsp-/colleges_divisions/military/veterans/jcr:content/contentParsys/section/row_1077504772/column/image"]/img') #imagem do John
  alt_veteran = veteran_image.get_property('alt')  #recebe o atributo ALT da imagem
  sleep(1)
  assert alt_veteran == 'JohnLEstrada_SmallSize_reducedNoise' #verifica se alt é JohnLEstrada_SmallSize_reducedNoise
  sleep(2)

# 6 TESTA 4 ITEMS DA LISTA DESORDENADA! 4 li da ul
def test_account(browser):
  actions = ActionChains(browser) #cria uma fila de ações
  botao_degree = browser.find_element_by_xpath('//*[@id="degree"]') #botão Degree & Programs
  actions.click(botao_degree) #clica no botao /fila
  actions.perform() #executa a fila
  sleep(1) #dormir 5 segundos
  #abriu megamenu
  actions = ActionChains(browser) #cria uma fila de ações
  accounting = browser.find_element_by_xpath('//*[@id="Bachelor_s_Business_0"]') #botão Accounting
  actions.click(accounting) #clica no Botão /fila
  actions.perform() #executa a fila
  sleep(1) 
  #pegando UL do site: Full_xpath /html/body/div[2]/div/div[2]/div/section[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[2]/ul
  account_ul = browser.find_element_by_xpath('//*[@id="overview"]/div/div/div/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[2]/ul')
  list_item = account_ul.find_elements_by_tag_name('li') #pega os items da listav    
  assert list_item[0].text == 'Accounting'                                   #testa se é account..
  assert list_item[1].text == 'Auditing'                                     #testa se é Auditing
  assert list_item[2].text == 'Financial Statements'                         #testa se é Financial Statements
  assert list_item[3].text == 'Generally Accepted Accounting Principles'     #testa se é Generally Accepted Accounting Principles
  actions = ActionChains(browser) #cria uma fila de ações
  # actions.move_to_element_with_offset(list_item[3],0,10).perform() #move pro quarto item da lista
  sleep(2)

# 7 TESTA A EXISTENCIA DE UM CURSO NETWORK SECURITY
def test_course(browser):
  actions = ActionChains(browser) #cria a fila de ações
  botao_search = browser.find_element_by_xpath('//*[@id="search-link-open"]') #botao Search
  actions.click(botao_search) #clica botao Search /fila     
  actions.perform() #executa a fila
  sleep(1)
  actions = ActionChains(browser) #cria a fila de ações
  #pesquisando por cursos
  find_course = browser.find_element_by_xpath('//*[@id="upox-search-input"]') #pega o input do pesquisar
  find_course.send_keys('Network Security') #insere Network ...
  actions.key_down(Keys.ENTER).perform() #tecla enter
  sleep(5) #necessário 5
  result = browser.find_element_by_id('courseItem_0') #pega o primeiro resultado ID0
  sleep(2)
  title = result.find_element_by_tag_name('h2') #pega o H2 do primeiro resultado
  sleep(2)
  assert title.text == 'NETWORK SECURITY' #testa se é NETWORK ..

# 8 TEST FOOTER - TESTA SE A NAV DO FOOTER TEM DETERMINADA CLASSE
def test_footer(browser):
  footer = browser.find_element_by_tag_name('footer') #pega o Footer da página
  sleep(2)
  footer_nav = footer.find_element_by_tag_name('nav') #pega um Nav do Footer
  sleep(1)
  propriedade = "footer-nav" in footer_nav.get_attribute("class") #verifica se tem a classe
  sleep(1)
  assert propriedade == True #verifica se propriedade é igual a TRUE

# 9 TEST ACORDIAN 
def test_acordian(browser):
  actions = ActionChains(browser) #cria a fila de ações
  acordian = browser.find_element_by_xpath('//*[@id="tabpanel-185112224-1"]/div/div/div[1]/div/a/span') #Botao +
  sleep(1)
  browser.execute_script("arguments[0].click();", acordian) #clica no acordian
  sleep(1)
  span = "activeTab" in acordian.get_attribute("class") #verifica se tem a classe
  sleep(1)
  assert span == True #verifica se propriedade é igual a TRUE
  title = browser.find_element_by_xpath('//*[@id="tabpanel-185112224-1"]/div/div/div[1]/div/a/h3') #pega o titulo
  cor = title.value_of_css_property('color') #pega a cor
  sleep(1)
  print(cor)
  assert cor == 'rgba(219, 55, 37, 1)' #testa a cor

# 10 TEST REQUEST INFO
def test_request(browser):
  request = browser.find_element_by_xpath('//*[@id="globalNavigationWrapper"]/nav/div[2]/div[1]/div[4]/a[2]') #botão laranja Request Info
  browser.execute_script("arguments[0].click();", request) #clica no request
  sleep(3) #precisa ser 3!
  select = browser.find_element_by_tag_name('select') #pega botao select
  #actions.click(botao_search) #clica botao Search /fila    
  items_select = Select(select)
  sleep(1)
  items_select.select_by_visible_text('Brazil') #seleciona Brazil
  sleep(3)
  assert select.get_property('value') == 'BR' #compara se SELECT é Brazil