#encrypted_file = open("encrypted_message_two.txt", 'r')

#encrypted_message = encrypted_file.readline()

#encrypted_file.close()

# Write Code Here
encrypted_message = 'Tgeoq ooe bb oo  vohwtynis,o" niissaemwsth  unrhn  oa aaswion eamntioaoaopiesni  dhvtrt eeiip cm EfDcEn eutyan  w"rtnssa as uedwres ieacee nipcd ehi irnbseg isnmtcr douefc mcllxr  tttdmesewp onno rocdls bqnaieacurcehaii nowttl raos ttou eayet enriccimel te ia aAo. eapkoo  rnmehsua dinm leosptevt eenesddntimstbeteenn dits eeesa.aIl uoxrtRoA Mo.tdafml ,hp oaitesa  exgllndthoe  scte ch ttydutteirkcthii  euns  tAd es  oa laGemtT ye ttoul nh.'
encrypted_list = [c for c in encrypted_message]
decrypted_message = ''
for l in range(0, len(encrypted_list)//2):
    if l % 2 == 1:
        place_holder = encrypted_list[l]
        encrypted_list[l] = encrypted_list[-l-1]
        encrypted_list[-1-l] = place_holder
decrypted_message= ''.join(encrypted_list)
print(decrypted_message)

        
