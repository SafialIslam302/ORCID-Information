import restfull
import json


with open('input_file_1.txt') as f:
    lines = [line.rstrip() for line in f]


for line in lines:
    orcid_res = restfull.get(line)

    #print(orcid_res.publications)

    publication_number = len(orcid_res.publications)
    education_number = len(orcid_res.educations)
    employment_number = len(orcid_res.employments)
    #print(n)
    #print(orcid_res.publications[15].title)

    #file = orcid_res.family_name + "_" + orcid_res.given_name + "_" + line

    file_name = "%s.txt" % line

    #outputfile = output_path + "/" + file_name
    #print(outputfile)

    output_file_name = "Result/" + file_name

    with open(output_file_name, 'w', encoding='utf-8') as output:
        print("Running: " + orcid_res.orcid)
        output.writelines("ORCID: " + orcid_res.orcid + "\n")
        output.writelines("Family Name: " + orcid_res.family_name + "\n")
        output.writelines("Given Name: " + orcid_res.given_name + "\n")
        output.writelines("\n")

        output.writelines("Number of Works: " + str(publication_number) + "\n")
        output.writelines("\n")
        output.writelines("Work Details")
        output.writelines("\n")

        for i in range(publication_number):
            print("\nWork No: " + str(i + 1) + "\n")
            output.writelines("\nWork No: " + str(i + 1) + "\n")
            try:
                if orcid_res.publications[i].citation_value is None:
                    output.writelines(orcid_res.publications[i].title) #orcid_res.publications[i].title/No thing Found
                    output.writelines("\n\n")
                else:
                    output.writelines(orcid_res.publications[i].citation_value)
                    output.writelines("\n")
            except ValueError:
                try:
                    if orcid_res.publications[i].title is None:
                        output.writelines("No Information found") #orcid_res.publications[i].title/No thing Found
                        output.writelines("\n\n")
                    else:
                        output.writelines(orcid_res.publications[i].title)
                        output.writelines("\n\n")
                except ValueError:
                    output.writelines("No Information found")
                    output.writelines("\n")

            output.writelines("\n\n")

        output.writelines("Number of education: " + str(education_number) + "\n")
        output.writelines("\n")
        output.writelines("Education Details")
        output.writelines("\n")


        for j in range(education_number):
            output.writelines(str(j+1) + " " + orcid_res.educations[j] + "\n")


        output.writelines("\n\n")

        output.writelines("Number of employment: " + str(employment_number) + "\n")
        output.writelines("\n")
        output.writelines("Employment Details")
        output.writelines("\n")

        for k in range(employment_number):
            output.writelines(str(k+1) + " " + orcid_res.employments[k] + "\n")

        print("Finish: " + orcid_res.orcid)
