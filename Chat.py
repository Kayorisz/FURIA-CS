import unicodedata
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

def removeacentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def resposta(msg):
    msg = msg.lower()
    if "oi" in msg or "ola" in msg or "eae" in msg or "eai" in msg or "e ai" in msg:
        return "Oi! Como posso ajudar?"
    elif ("como" in msg and "esta" in msg) or ("como" in msg and "vai" in msg):
        return "Estou ótimo, obrigado por perguntar! Como posso te ajudar hoje?"
    
    elif "furia" in msg:
        return "A FURIA foi fundada em 2017 e rapidamente se destacou no cenário de esportes eletrônicos, especialmente no CS:GO. A equipe brasileira conquistou reconhecimento internacional com um estilo de jogo agressivo e inovador. Hoje, a FURIA é uma das organizações mais respeitadas, representando o Brasil em grandes torneios e conquistando fãs ao redor do mundo."
    elif "cs" in msg or "counter" in msg and "strike" in msg:
        return "A FURIA é um dos melhores times de CS, atualmente! O time já ganhou duas Premiers e vários outros campeonatos importantes!"
    elif "major" in msg:
        return "O time ainda não venceu nenhum Major oficial da Valve, mas segue dedicando ao máximo para conquistar esse título!"
    elif "premier" in msg:
        return "O time já ganhou duas Premiers e segue em busca de mais títulos!"
    
    elif "elenco" in msg or "lineup" in msg or "escalação" in msg or "time" in msg:
        return "O elenco atual do time da FURIA é composto por: Fallen como líder e AWPer; KSCERATO, yuurih e molodoy como Rifler; YEKINDAR como Stand-In; skullz e chelo como reserva; e sidde como treinador."
    elif "fallen" in msg or "igl" in msg or "leader" in msg or "lider" in msg or "awper" in msg or "gabriel" in msg or "gabriel" in msg and "toledo" in msg:
        return "Gabriel 'Fallen' Toledo é o líder dentro e fora do servidor da FURIA, exercendo a função de AWPer e IGL desde julho de 2023."
    elif "yuurih" in msg or "yuri" in msg or "boian" in msg:
        return "Yuri 'yuurih' Boian veste a camisa da FURIA desde 2017, sendo um dos riflers mais consistentes do time."
    elif "kscerato" in msg or "kaike" in msg or "cerato" in msg:
        return "Kaike 'KSCERATO' Cerato é um dos pilares da FURIA desde 2018, jogando como rifler e sendo peça-chave do elenco."
    elif "molodoy" in msg or "danil" in msg or "golubenko" in msg:
        return "Danil 'molodoy' Golubenko se juntou à FURIA em abril de 2025, trazendo talento e experiência para a função de rifler."
    elif "yekindar" in msg or "mareks" in msg:
        return "Mareks 'yekindar' Gaļinskis atua como stand-in na FURIA desde abril de 2025, contribuindo com sua agressividade e leitura de jogo."
    elif "skullz" in msg or "felipe" in msg or "medeiros" in msg:
        return "Felipe 'skullz' Medeiros entrou para a reserva da FURIA em julho de 2024, sendo uma das promessas do CS brasileiro."
    elif "chelo" in msg or "marcelo" in msg or "cespedes" in msg:
        return "Marcelo 'chelo' Cespedes faz parte do banco da FURIA desde julho de 2023, pronto para contribuir quando necessário."
    elif "treinador" in msg or "sidde" in msg or "sidney" in msg or "macedo" in msg:
        return "Sidney 'sidde' Macedo é o head coach da FURIA desde julho de 2024, liderando a equipe fora dos servidores com muita estratégia."
    
    elif  "jogador" in msg and "antigo" in msg or "ex" in msg and "jogador" in msg:
        return "A FURIA já contou com grandes nomes no CS ao longo dos anos! Jogadores como HEN1, arT, VINI, ableJ e chelo marcaram história com a camisa da equipe antes de seguirem novos caminhos. Cada um deixou sua marca — e a torcida nunca esquece!"
    elif "art" in msg or "andrei" in msg or "piovezan" in msg:
        return "Andrei 'arT' Piovezan foi o capitão da FURIA por muitos anos, conhecido por seu estilo agressivo e tático. Em abril de 2024, foi movido para o banco de reservas após uma longa trajetória na equipe."
    elif "vini" in msg or "vinicius" in msg or "figueiredo" in msg:
        return "Vinicius 'VINI' Figueiredo atuou como rifler na FURIA, sendo peça-chave em diversas conquistas da equipe. Deixou o time em 2022 para buscar novos desafios."
    elif "hen1" in msg or "henrique" in msg or "teles" in msg:
        return "Henrique 'HEN1' Teles foi o AWPer da FURIA durante um período importante, contribuindo com sua mira precisa. Saiu da equipe em 2021."
    elif "ablej" in msg or "rinaldo" in msg or "moda" in msg:
        return "Rinaldo 'ableJ' Moda foi um dos primeiros jogadores da FURIA, ajudando na ascensão da equipe no cenário internacional. Deixou o time em 2019."
    elif "junior" in msg or "paytyn" in msg or "johnson" in msg:
        return "Paytyn 'junior' Johnson, jogador norte-americano, atuou como AWPer na FURIA em 2021, trazendo uma perspectiva internacional ao time."
    elif "honda" in msg or "lucas" in msg:
        return "Lucas 'Honda' Honda teve uma breve passagem pela FURIA em 2021, sendo promovido da equipe Academy para o elenco principal."
    elif "guerri" in msg or "nicholas" in msg or "nogueira" in msg:
        return "Nicholas 'guerri' Nogueira foi o treinador da FURIA por vários anos, desempenhando um papel fundamental no desenvolvimento da equipe. Em abril de 2024, assumiu a posição de Head de Esports da organização."
    elif "spacca" in msg or "guilherme" in msg:
        return "Guilherme 'spacca' Spacca foi um dos primeiros jogadores da FURIA, integrando a equipe em 2017 durante sua formação inicial."
    elif "prd" in msg or "arthur" in msg or "resende" in msg:
        return "Arthur 'prd' Resende fez parte da formação inicial da FURIA em 2017, contribuindo para os primeiros passos da equipe no cenário competitivo."
    elif "sllayer" in msg or "bruno" in msg or "silva" in msg:
        return "Bruno 'Sllayer' Silva integrou a formação original da FURIA em 2017, participando das primeiras competições da equipe."
    elif "caike" in msg or "costa" in msg:
        return "Caike 'caike' Costa foi um dos membros fundadores da FURIA em 2017, fazendo parte do elenco inicial da equipe."
    elif "bld" in msg or "victor" in msg or "junqueira" in msg:
        return "Victor 'bld' Junqueira teve uma breve passagem pela FURIA em 2017, contribuindo durante o período de transição da equipe."
    elif "s1" in msg or "ricardo" in msg or "shinji" in msg:
        return "Ricardo 's1' Shinji integrou a FURIA em 2018, participando do processo de consolidação da equipe no cenário competitivo."

    elif "criacao" in msg or "fund" in msg or "criado" in msg:
        return "A FURIA foi fundada em agosto de 2017 por Jaime Pádua, André Akkari, Cristian Guedes e Nicholas Nogueira!"
    elif "proxima" in msg and "partida" in msg:
        return "Atualmente, a FURIA não tem nenhuma partida marcada, embora já tenha três torneios confirmados: o IEM Dallas 2025, o PGL Astana 2025 e o Austin Major 2025!"
    elif "proximo" in msg and "torneio" or "proximo" in msg and "campeonato" in msg:
        return "A FURIA já tem três torneios confirmados: o Austin Major 2025, o IEM Dallas 2025 e o PGL Astana 2025!"
    elif "partida" in msg and "recente" in msg or "partida" in msg and "anterior":
        return "A FURIA vem de uma sequência difícil, com 4 derrotas e 1 vitória! Ainda sim, o time mantém cerca de 65% de vitórias no últimos meses!"
    elif "map" in msg:
        return "O melhor mapa da FURIA é o Nuke, onde o time tem uma taxa de vitória de 71%. Eles também se destacam em Dust2 e Ancient, mas o Nuke é o seu mapa mais forte!"
    elif "ct" in msg or "contra" in msg and "terrorista" in msg or "contra" in msg:
        return "Atualmente a FURIA enfrenta dificuldades no lado Contra-Terrorista (CT),  acumulando várias derrotas em LANs em 2025."
    elif "terrorista" in msg or "tr" in msg:
        return "A FURIA, atualmente, tem mostrando um desempenho sólido no lado Terrorista (TR)!"
    
    elif "ultimo" in msg and "jogo" in msg:
        return "O último jogo da FURIA foi contra a equipe The MongolZ, e acabamos sendo derrotados."
    elif "momento" in msg:
        return "Confira os melhores momentos do time no nosso canal no nosso YouTube: youtube.com/furiagg!"
    elif "primeiro" in msg and "campeonato" in msg:
        return "O primeiro grande campeonato conquistado pela FURIA foi a ESEA Season 27: Global Challenge, em 2018. Essa vitória marcou o início da ascensão da equipe no cenário internacional."
    elif "dreamhack" in msg or "rio" in msg and "2019" in msg:
        return "A DreamHack Open Rio 2019 foi histórica para a FURIA. Jogando em casa, com o apoio da torcida brasileira, a equipe chegou à final e consolidou seu nome como uma potência em ascensão."
    elif "ecs" in msg and "season 7" in msg or "final" in msg and "2019" in msg:
        return "A FURIA brilhou nas finais da ECS Season 7 em 2019, enfrentando as melhores equipes do mundo e mostrando um CS agressivo e único que chamou a atenção do cenário internacional."
    elif "esl" in msg and "pro league" in msg and "2020" in msg:
        return "Em 2020, a FURIA venceu a ESL Pro League Season 12: América do Norte. Foi um título muito importante em plena pandemia, reafirmando a força da equipe no cenário americano."
    elif "iem" in msg and "new york" in msg and "2020" in msg:
        return "A FURIA conquistou o título da IEM New York 2020 na região da América do Norte, vencendo times de alto nível e mostrando sua consistência e evolução no cenário competitivo."
    elif "melbourne" in msg or "esl challenger" in msg and "2022" in msg:
        return "A vitória no ESL Challenger Melbourne em 2022 foi mais uma conquista internacional da FURIA, reforçando o nome da organização como uma das potências brasileiras no CS."
    elif "campeonato" in msg:
        return (
            "A FURIA construiu sua história com conquistas marcantes ao longo dos anos! "
            "Tudo começou com o título da ESEA Season 27: Global Challenge em 2018, que marcou a estreia internacional do time. "
            "Depois vieram campanhas memoráveis como a DreamHack Rio 2019, a grande performance na ECS Season 7 Finals, "
            "e os títulos na ESL Pro League Season 12 e na IEM New York 2020 – ambos na América do Norte. "
            "Mais recentemente, a FURIA venceu o ESL Challenger Melbourne em 2022, consolidando ainda mais seu nome no cenário mundial. "
            "Cada campeonato representa um capítulo especial da nossa trajetória!"
        )

        
    elif "camisa" in msg or "uniforme" in msg:
        return "Você pode adquirir o uniforme oficial do time no site: furia.gg!"
    elif "rede" in msg or "rede" in msg and "socia" in msg:
        return ("Aqui estão as redes sociais oficiais da FURIA:\n\n"
        "Instagram: https://www.instagram.com/furiagg\n"
        "Twitter/X: https://twitter.com/furiagg\n"
        "TikTok: https://www.tiktok.com/@furia\n"
        "YouTube: https://www.youtube.com/furiagg\n"
        "Facebook: https://www.facebook.com/furia.gg\n\n"
        "Siga a FURIA e fique por dentro de todas as novidades!")
    elif "discord" in msg or "servidor" in msg or "server" in msg:
        return "Venha participar do Discord da FURIA e faça parte da nossa comunidade furiosa! Lá rola bate-papo, eventos e novidades exclusivas: discord.gg/furiagg"
    elif "youtube" in msg or "video" in msg:
        return "Quer ver os bastidores, jogadas incríveis e vídeos especiais da FURIA? Nosso canal no YouTube tá recheado de conteúdo! Se inscreve lá: youtube.com/furiagg"
    elif "twitch" in msg or "transmiss" in msg:
        return "Acompanhe as transmissões da FURIA ao vivo na Twitch! Jogos, torneios e muito conteúdo da nossa tropa te esperam: https://www.twitch.tv/furiatv"
    elif "instagram" in msg:
        return "A FURIA compartilha bastidores, conquistas e o dia a dia dos nossos atletas no Instagram! Acompanhe tudo de perto no nosso instagram: instagram.com/furiagg"
    elif "facebook" in msg:
        return "A FURIA também está no Facebook! Acesse para ver fotos, notícias e atualizações importantes da nossa organização: facebook.com/furiagg"
    elif "streamer" in msg:
        return "A FURIA conta com vários streamers como o Brino, Mount, Mwzera e Paula Nobre! Para ver todos, acesse nosso canal na Twitch: twitch.tv/furiatv"
    
    elif "patroci" in msg:
        return "A FURIA, atualmente no CS2, é patrocinada por Cruzeiro do Sul, PokerStars, Red Bull, Hellmann’s e Lenovo."
    elif "cruzeiro" in msg and "sul" in msg or "cruzeiro" in msg or "sul" in msg:
        return "A parceria com a Cruzeiro do Sul começou em 2023, reforçando a importância da educação nos eSports. A marca investe no crescimento profissional e acadêmico dos atletas da FURIA e na formação de fãs conscientes e preparados."
    elif "poker" in msg:
        return "Desde 2022, o PokerStars está com a FURIA, conectando o mundo das apostas e da estratégia com o cenário competitivo do CS2. A parceria trouxe campanhas criativas e aproximou ainda mais o público gamer da marca."
    elif "red" and "bull" in msg:
        return "Red Bull entrou como patrocinadora da FURIA em 2020. Presente em vários esportes radicais e eletrônicos, a marca dá energia e visibilidade ao time, apoiando também ações de conteúdo e performance."
    elif "hellma" in msg:
        return "Em 2023, Hellmann’s se uniu à FURIA com uma abordagem divertida e original. A marca já marcou presença em conteúdos especiais com os jogadores e trouxe ainda mais sabor ao mundo gamer."
    elif "lenovo" in msg:
        return "Parceira desde 2022, a Lenovo equipa a FURIA com computadores e tecnologia de ponta, garantindo que a equipe jogue com a melhor performance possível nos campeonatos de CS2."

    elif "sair" in msg:
        return "Ok, até mais! Se precisar de algo, é só chamar!"
    else:
        return "Desculpe, não entendi."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Eu sou o assistente da FURIA! Vamos bater um papo?\nSe deseja encerrar a conversa, apenas digite \"sair\"')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = resposta(user_message)
    await update.message.reply_text(response)

    if "Ok, até mais!" in response:
        await context.application.stop()

def main():
    application = ApplicationBuilder().token("7275349469:AAHuG43GqnG0jGaKdd8uA-WlBV5aUmO3xFs").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()