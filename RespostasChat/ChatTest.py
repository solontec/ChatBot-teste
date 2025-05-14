def responder(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Olá! Estou aqui para te ajudar com oratória. Pergunte o que quiser!"
    
    elif "o que é oratória" in mensagem:
        return "Oratória é a arte de falar bem em público, com clareza, persuasão e impacto."

    elif "como perder o medo de falar em público" in mensagem:
        return ("Uma boa forma de perder o medo é praticar bastante, conhecer bem o conteúdo, "
                "respirar fundo antes de começar e fazer simulações com amigos ou no espelho.")

    elif "dicas para falar melhor" in mensagem:
        return ("Claro! Aqui vão algumas dicas:\n"
                "- Organize suas ideias antes de falar\n"
                "- Fale com clareza e articule bem as palavras\n"
                "- Use pausas estratégicas\n"
                "- Mantenha contato visual\n"
                "- Adapte sua fala ao público")

    elif "como melhorar a dicção" in mensagem:
        return ("Você pode treinar com trava-línguas, ler textos em voz alta lentamente, "
                "gravar sua voz e corrigir a pronúncia. Exercícios com a boca e língua também ajudam!")

    elif "o que é storytelling" in mensagem:
        return ("Storytelling é a técnica de contar histórias de forma envolvente, usada em oratória para capturar "
                "a atenção do público e tornar a mensagem mais memorável.")

    elif "exercícios de oratória" in mensagem:
        return ("Alguns bons exercícios são:\n"
                "- Ler em voz alta\n"
                "- Gravar suas falas e assistir depois\n"
                "- Improvisar sobre temas aleatórios por 1 minuto\n"
                "- Praticar apresentações em frente ao espelho ou para amigos")

    elif "como controlar o nervosismo" in mensagem:
        return ("Respiração profunda, preparação antecipada e mentalização positiva ajudam muito. "
                "Também é importante aceitar que sentir um pouco de nervosismo é normal!")

    elif "tchau" in mensagem or "adeus" in mensagem:
        return "Até logo! Continue praticando sua oratória."

    else:
        return "Desculpa, não entendi muito bem. Pergunte algo relacionado a oratória :)"

def iniciar_chat():
    print("=== Chatbot de Oratória ===")
    print("Digite 'sair' para encerrar.\n")

    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == "sair":
            print("Chatbot: Foi um prazer te ajudar. Até a próxima!")
            break
        resposta = responder(mensagem)
        print("Chatbot:", resposta)

# Início do chatbot
iniciar_chat()
