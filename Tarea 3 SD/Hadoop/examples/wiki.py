import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName', 'es')
for i in range(10):
 busqueda = input("ingresar busqueda: ")
 page_py = wiki_wiki.page(busqueda)
 print("Page - Exists: %s" % page_py.exists())


 page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
 print("Page - Exists: %s" %     page_missing.exists())

 print("Page - Title: %s" % page_py.title)
    
 print("Page - Summary: %s" % page_py.summary[0:60])
   
 print(page_py.fullurl)


 print(page_py.canonicalurl)

 wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='MyProjectName (merlin@example.com)',
        language='es',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

 p_wiki = wiki_wiki.page(busqueda)
 print(p_wiki.text)

 with open(busqueda+".txt", 'w', encoding='utf-8') as file:
    for item in p_wiki.text:
        file.write(item)