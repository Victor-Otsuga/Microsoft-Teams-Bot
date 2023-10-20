import pymsteams
import time

def send_teams_message_with_delay():
    # Crie a mensagem
    myTeamsMessage = pymsteams.connectorcard("https://etecspgov.webhook.office.com/webhookb2/31bbf84f-0bad-40b7-aba6-a138fad02317@ed38466c-b641-437d-9ae9-d801b829fa94/IncomingWebhook/b1b64bb50da34d829730c85cf8626c30/77ddb707-71fe-488c-af99-235e1329dd8f")
    myTeamsMessage.text("Mensagem teste")
    
    # Aguarde 10 segundos
    time.sleep(10)
    
    # Envie a mensagem
    myTeamsMessage.send()

# Chame a função para enviar a mensagem com atraso de 10 segundos
send_teams_message_with_delay()
