import discord
from discord.ext import commands
import os
from model import get_class
intents = discord.Intents.default()
intents.message_content = True
IMAGE_DIR="images"
os.makedirs(IMAGE_DIR, exist_ok=True)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def analiz(ctx):
    if ctx.message.attachments :
        for attachment in ctx.message.attachments:
            file_name= attachment.filename
            file_path= os.path.join(IMAGE_DIR, file_name)
            await attachment.save(file_path)
            await ctx.send("görsel basariyla kaydoldu")
            class_name, score = get_class(file_path)
            await ctx.send(f"Görselinizin sinifi:{class_name}, ve tahmin puani:{score:.0%}")
            information = {
    "Plastik": (
        "Doğada Kaybolma Süresi: 450 – 1000 yıl.\n\n"
        'Önemli Bilgi: Plastikler doğada tamamen yok olmaz; "mikroplastik" adı verilen küçük parçalara bölünerek su kaynaklarımıza ve besin zincirimize karışır.\n\n'
        "Geri Dönüşüm Faydası: 1 ton plastiğin geri dönüştürülmesiyle 5.774 kWh enerji tasarrufu sağlanır ve 16.3 varil petrol kullanımı engellenir."
    ),
    "Kagit/ Karton": (
        "Doğada Kaybolma Süresi: 2 – 6 hafta.\n\n"
        "Önemli Bilgi: Kağıt üretimi için yüksek miktarda ağaç kesilir ve su harcanır. Kağıdı geri dönüştürmek ormanları korumanın en doğrudan yoludur.\n\n"
        "Geri Dönüşüm Faydası: 1 ton atık kağıdın geri dönüştürülmesi 17 yetişkin ağacın kesilmesini önler ve su tüketiminde %60 tasarruf sağlar."
    ),
    "Metal": (
        "Doğada Kaybolma Süresi: 80 – 200 yıl (Alüminyum kutular için).\n\n"
        "Önemli Bilgi: Alüminyum, kalitesinden hiçbir şey kaybetmeden sonsuz kez geri dönüştürülebilen nadir maddelerden biridir.\n\n"
        "Geri Dönüşüm Faydası: 1 adet alüminyum kutunun geri dönüştürülmesiyle elde edilen enerji, bir televizyonu 3 saat boyunca çalıştırmaya yeter."
    ),
    "Yiyecek atik": (
        "Doğada Kaybolma Süresi: 2 hafta – 6 ay (Meyve kabukları ortalama 2-5 hafta, pişmiş yemek artıkları ve kemikler 6 aya kadar sürebilir).\n\n"
        "Önemli Bilgi: Yiyecek atıkları çöplüklere (vahşi depolama alanlarına) gittiğinde oksijensiz ortamda çürür ve karbondioksitten 28 kat daha zararlı olan Metan gazı (CH4) açığa çıkarır. Bu durum küresel ısınmayı doğrudan tetikler.\n\n"
        "Geri Dönüşüm Faydası (Kompost): Organik atıklar çöpe gitmek yerine kompost (doğal gübre) yöntemiyle toprağa dönüştürülebilir. Kompost yapımı toprağın verimini artırır, kimyasal gübre ihtiyacını sıfırlar ve toprağın su tutma kapasitesini yükseltir."
    ),
}
            info=information.get(class_name)
            await ctx.send(info)
    else:
        await ctx.send("lütfen görsel gönderiniz")


bot.run("")