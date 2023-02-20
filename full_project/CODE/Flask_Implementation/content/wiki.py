import wikipedia
import pandas as pd
import csv
import os 
import matplotlib.pyplot as plt
import requests
import shutil

df = pd.read_csv('birds.csv')
LABELS = df['labels'].unique()
labels = list(map(str.lower,LABELS))
result = wikipedia.search("american bittern", results = 5)
print(result)
print(len(labels))
i = 0
f = f = open('wiki_info.csv', 'w')
writer = csv.writer(f)
writer.writerow(['label', 'info', 'image path', 'page url'])
img_dir = "images"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

headers = {'User-Agent': 'MichaelJames(majames425@gmail.com)'}



for i in range(i, len(labels)):
    label = labels[i]
    x1 = label.replace("alberts towhee", "aberts towhee")
    x1 = x1.replace("american bittern", "Botaurus lentiginosus")
    x1 = x1.replace("american flamingo", "Phoenicopterus ruber")
    x1 = x1.replace("american goldfinch", "Spinus tristis")
    x1 = x1.replace("american redstart", "Setophaga ruticilla")
    x1 = x1.replace("ashy thrushbird", "ashy thrush")
    x1 = x1.replace("asian dollard bird", "Oriental dollarbird")
    x1 = x1.replace("bali starling", "Bali myna")
    x1 = x1.replace("barn owl", "Tyto alba")
    x1 = x1.replace('black cockatoo', 'Glossy black cockatoo')
    x1 = x1.replace("black skimmer", "Rynchops niger")
    x1 = x1.replace("black swan", "Cygnus atratus")
    x1 = x1.replace("brandt cormarant", "cormarant")
    x1 = x1.replace('canary', 'Atlantic canary')
    x1 = x1.replace("capuchinbird", "calfbird")
    x1 = x1.replace("cedar waxwing", "Bombycilla cedrorum")
    x1 = x1.replace("chestnet bellied euphonia", "Euphonia pectoralis")
    x1 = x1.replace("cuban tody", "Todus multicolor")
    x1 = x1.replace("curl crested aracuri", "Pteroglossus beauharnaisii")
    x1 = x1.replace("double brested cormarant", "Phalacrocorax lucidus")
    x1 = x1.replace("emu", "Dromaius novaehollandiae")
    x1 = x1.replace("frigate", "Frigatebird")
    x1 = x1.replace("great potoo", "Nyctibius grandis")
    x1 = x1.replace("groved billed ani", "Crotophaga sulcirostris")
    x1 = x1.replace("inca tern", "Larosterna inca")
    x1 = x1.replace("indian bustard", "Ardeotis nigriceps")
    x1 = x1.replace("kiwi", "Apteryx mantelli")
    x1 = x1.replace("iwi", "scarlet honeycreeper")
    x1 = x1.replace("masked booby", "Sula dactylatra")
    x1 = x1.replace("kagu", "Rhynochetos jubatus")
    x1 = x1.replace("kakapo", "Strigops habroptilus")
    x1 = x1.replace("maleo", "Macrocephalon maleo")
    x1 = x1.replace("myna", "Acridotheres tristis")
    x1 = x1.replace("northern flicker", "Colaptes auratus")
    x1 = x1.replace("northern gannet", "Morus bassanus")
    x1 = x1.replace("orange brested bunting", "Passerina leclancherii")
    x1 = x1.replace("paradise tanager", "Tangara chilensis")
    x1 = x1.replace("parakett  akulet", "Aethia psittacula")
    x1 = x1.replace("parus major", "great tit (Parus major) ")
    x1 = x1.replace("philippine eagle", "Pithecophaga jefferyi")
    x1 = x1.replace("pygmy kingfisher", "Ispidina picta")
    x1 = x1.replace("quetzal", "disambiguation")
    x1 = x1.replace("red wiskered bulbul", "Pycnonotus jocosus")
    x1 = x1.replace("roadrunner", "genus Geococcyx")
    x1 = x1.replace("robin", "Turdus migratorius")
    x1 = x1.replace("rock dove", "rock pigeon")
    x1 = x1.replace("samatran thrush", "Sumatran laughingthrush")
    x1 = x1.replace("sandhill crane", "Antigone canadensis")
    x1 = x1.replace("spoon biled sandpiper", "Calidris pygmaea")
    x1 = x1.replace("spoonbill", "disambiguation")
    x1 = x1.replace("stripped swallow", "Cecropis abyssinica")
    x1 = x1.replace("teal duck", "Anas crecca")
    x1 = x1.replace("turkey vulture", "Cathartes aura")
    x1 = x1.replace("whimbrel", "Numenius hudsonicus")
    x1 = x1.replace("white browed crake", "Poliolimnas cinereus")
    x1 = x1.replace("wild turkey", "Meleagris gallopavo")
    
    print(label)
    img = ''
    try:
        info = wikipedia.summary(x1, sentences=2)
        images = wikipedia.page(x1).images
        for img in images:
            if img.endswith('.jpg'):
                break
        url = wikipedia.page(x1).url
        img_filename = f"{img_dir}/{'_'.join(x1.split(' '))}.jpg"
        res = requests.get(img, stream=True, headers=headers)
        if res.status_code == 200:
            with open(img_filename, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
        else:
            print("request not successfull")
    except:
        l2 = wikipedia.search(x1, results = 5)[1]
        info = wikipedia.summary(l2, sentences=2)
        # img = wikipedia.page(l2).images[0]
        url = wikipedia.page(l2).url
    if len(img) == 0:
        img= "NO IMG"

    print(info)
    print(img)
    print(url)

    i+=1
    print(i, "**************************************")
    row = [label, info, img, url]
    writer.writerow(row)
    non_valid = ['mp3','ogg', 'ogv', 'tif', 'ogg', 'png', 'svg', 'NO IMG']
f.close()
