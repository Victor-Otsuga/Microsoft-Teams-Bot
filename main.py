import time
from pymsteams import connectorcard

while True:
  # Crie a mensagem
  myTeamsMessage = connectorcard("https://etecspgov.webhook.office.com/webhookb2/31bbf84f-0bad-40b7-aba6-a138fad02317@ed38466c-b641-437d-9ae9-d801b829fa94/IncomingWebhook/b1b64bb50da34d829730c85cf8626c30/77ddb707-71fe-488c-af99-235e1329dd8f")
  myTeamsMessage.text("Mensagem teste")
  
  # Envie a mensagem após o atraso de 10 segundos
  myTeamsMessage.send()

  # Aguarde 10 segundos
  time.sleep(10)
