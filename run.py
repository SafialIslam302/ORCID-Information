import restfull
import json

with open('input_file.txt') as f:
    lines = [line.rstrip() for line in f]


for line in lines:
    orcid_res = restfull.get(line)

    publication_number = len(orcid_res.publications)
    employment_number = len(orcid_res.employments)

    file_name = "%s.txt" % line
    
    # Please make sure you create a Result folder. 
    # The output will save in the Result folder

    output_file_name = "Result/" + file_name

    with open(output_file_name, 'w', encoding='utf-8') as output:
        print("ID Running: " + orcid_res.orcid)
        output.writelines("ORCID: " + orcid_res.orcid + "\n")
        output.writelines("Family Name: " + orcid_res.family_name + "\n")
        output.writelines("Given Name: " + orcid_res.given_name + "\n")
        output.writelines("\n")

        output.writelines("Number of Works: " + str(publication_number) + "\n")
        output.writelines("\n")

        for i in range(publication_number):
            output.writelines("\n")
            output.writelines("\nWork Details No: " + str(i + 1) + "\n")
            try:
                if orcid_res.publications[i].title is None:
                    output.writelines("No Information found")
                    output.writelines("\n")
                else:
                    data = orcid_res.publications[i].url
                    #res_dct = {k:v for e in data for (k,v) in e.items()}
                    try:
                        #doi_url = list(res_dct['external-id-url'].values())
                        doi_url = list(data.values())
                        output.writelines("Paper title: " + orcid_res.publications[i].title + "\n")
                        output.writelines("Paper URL: " + doi_url[0])
                        output.writelines("\n")
                    except (AttributeError, KeyError) as e:
                        #doi_value = res_dct['external-id-value']
                        output.writelines("Paper title: " + orcid_res.publications[i].title + "\n")
                        output.writelines("No Paper URL found.")
                        output.writelines("\n")
            except (ValueError, KeyError) as e:
                output.writelines("Paper title: " + orcid_res.publications[i].title)
                output.writelines("\n")

            #time.sleep(1)

        output.writelines("\n\n")

        #output.writelines("Number of employment: " + str(employment_number) + "\n")
        #output.writelines("\n")

        for k in range(employment_number):
            #output.writelines("Current Employee\n")
            if(str(orcid_res.employments[k]['end-date']) == 'None'):
                output.writelines("Current Employee\n")
                output.writelines("Department name : " + str(orcid_res.employments[k]['department-name']))
                output.writelines("\nRole : " + str(orcid_res.employments[k]['role-title']))
                output.writelines("\nOrganization : " + str(orcid_res.employments[k]['organization']['name']))
                output.writelines("\nAddress : " + str(orcid_res.employments[k]['organization']['address']['city']))
                output.writelines("\n\n")

        print("ID Finish: " + orcid_res.orcid)
