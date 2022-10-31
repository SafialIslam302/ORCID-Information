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
        print("ID Running: " + orcid_res.orcid)
        output.writelines("ORCID: " + orcid_res.orcid + "\n")
        output.writelines("Family Name: " + orcid_res.family_name + "\n")
        output.writelines("Given Name: " + orcid_res.given_name + "\n")
        output.writelines("\n")

        output.writelines("Number of Works: " + str(publication_number) + "\n")
        output.writelines("\n")
        output.writelines("Work Details")
        output.writelines("\n")

        
        for j in range(education_number):
            #print(type(j))
            output.writelines("Education Details: " + str(j+1))
            #temp_education = orcid_res.educations[j]
            #print(orcid_res.educations[j])
            output.writelines("\n")
            #print(type(orcid_res.educations[j]))
            output.writelines("Department name : " + str(orcid_res.educations[j]['department-name']))
            output.writelines("\nRole : " + str(orcid_res.educations[j]['role-title']))
            output.writelines("\nOrganization : " + str(orcid_res.educations[j]['organization']['name']))
            output.writelines("\nAddress : " + str(orcid_res.educations[j]['organization']['address']['city']))          
            output.writelines("\n\n")

        output.writelines("\n\n")

        output.writelines("Number of employment: " + str(employment_number) + "\n")
        output.writelines("\n")

        for k in range(employment_number):
            output.writelines("Employmenr Details: " + str(k+1))
            #print(orcid_res.employments[k])
            #temp_employment = orcid_res.employments[k]
            output.writelines("\n")
            output.writelines("Department name : " + str(orcid_res.employments[k]['department-name']))
            output.writelines("\nRole : " + str(orcid_res.employments[k]['role-title']))
            output.writelines("\nOrganization : " + str(orcid_res.employments[k]['organization']['name']))
            output.writelines("\nAddress : " + str(orcid_res.employments[k]['organization']['address']['city']))
            output.writelines("\n\n")

        print("Finish: " + orcid_res.orcid)
