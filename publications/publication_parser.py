import json
import os 

def insert_papers(f, papers):
    last_year = 0
    for j in papers["journals"]:
        year = j["year"]
        if year != last_year:
            f.write("                    <h4>"+str(year)+":</h4>\n")
        f.write("                      <r><strong>"+j["title"]+"</strong> <br>\n")
        f.write("                      "+j["authors"].replace("E. Senft","<strong>E. Senft</strong>")+"<br>\n")
        f.write("                      "+j["journal"])
        if j["DOI"] == "":
            f.write(".<br>\n")
        else:
            f.write(", <a href=\""+j["DOI"]+"\" target=\"_blank\">DOI</a>.<br>\n")
        if j["pdf_address"] == "":
            f.write("PDF coming soon")
        else:
            f.write("                      <a href=\""+j["pdf_address"]+"\" target=\"_blank\">PDF</a>")
        f.write("<br>\n                  </r><hr>\n")
        last_year = year
    f.write("                  <h3>Conferences and Workshops</h3>\n")
    last_year=0
    for j in papers["conferences"]:
        year = j["date"].split(" ")[1]
        if year != last_year:
            f.write("                    <h4>"+str(year)+":</h4>\n")
        f.write("                      <r><strong>"+j["title"]+"</strong> <br>\n")
        f.write("                      "+j["authors"].replace("E. Senft","<strong>E. Senft</strong>")+"<br>\n")
        f.write("                      "+j["venue"] + " " + j["acronym"] + ", " + j["city"]+ ", " + j["country"]+", "+j["date"]+".<br>\n")
        if j["pdf_address"] == "":
            f.write("PDF coming soon")
        else:
            f.write("                      <a href=\""+j["pdf_address"]+"\" target=\"_blank\">PDF</a>")
        f.write("<br>\n                  </r><hr>\n")
        last_year = year
    

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/publications.json') as f:
        papers = json.load(f) 

    with open(dir_path + '/model.html') as f:
        model = f.readlines()

    with open(dir_path + '/../publication.html', "w") as f: 
        for line in model:
            if line[:-1] == "                  INSERT PUBLICATION":
                insert_papers(f, papers)
            else:
                f.write(line)