import requests

def send_simple_message(subject, text):
    mailgun_domain = 'sandbox98ebae98f8924ba7b83edc8ab6e49b08.mailgun.org'
    mailgun_api_key = 'MINHA_API_KEY'
    api_url = f"https://api.mailgun.net/v3/{mailgun_domain}/messages"

    try:
        response = requests.post(
            api_url,
            auth=("api", mailgun_api_key),
            data={
                "from": f"Aluno IFSP <mailgun@{mailgun_domain}>",
                "to": ["igor.ramosc1@gmail.com", "flaskaulasweb@zohomail.com"],
                "subject": subject,
                "text": text
            })

        response.raise_for_status()
        return 'E-mail enviado com sucesso!'
    except requests.exceptions.RequestException as e:
        return f'ERRO - Verifique se o seu e-mail está verificado na Mailgun'
