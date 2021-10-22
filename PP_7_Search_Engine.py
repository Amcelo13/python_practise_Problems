'''You are given given a few sentences as a list (Python list of sentences),You have to[[pull] out the
sentences mactching a query inputted by the user in [decreasing order] of relevance after converting every word
in the query and the sentence to lowercase
MOST RELEVANCE - Means maximum number of matching words with query
Senetence = ['This is good ,'python is good','python is not python snake']'''
def matchingWords(query ,sentence2):
    #.strip function to delete any spaces/word around a word  
    words1 = query.strip().split(" ")   #words1 and words2 will be a list made by the string.split(' ') 
    words2 = sentence2.strip().split(" ")
    matches = 0

    for i in words1:    #The every one element of outer loop applies to all elements of inner loop
        for j in words2:
            print(f'Matching {i} <=with=> {j}')
            if i.lower() == j.lower():
                matches += 1 
       
    return matches

if __name__ == '__main__':
    Sentences = ['python is good','this is snake','harry is a good boy subscribe' ,
                'subscribe to code with harry']

    query  = input('Enter your query string to search :')
    
    scores  = [matchingWords(query ,Sentence_list_element) for Sentence_list_element in Sentences]  #return values are the matches and as it is loop - > It forms matches list
#Scores is a list and say we take query = 'subscribe' then in 4th element of scores it shows 1 as a match
    print(scores)
#sorted_Sentence_score is a also a list but with zipped element of 'scores and Sentences' lists
    sorted_Sentence_score = [sentScore for sentScore in sorted
                             (zip(scores ,Sentences) , reverse= True) if sentScore[0] != 0]  #Means first element should not be 0/empty
    print(sorted_Sentence_score)
    print(f'{len(sorted_Sentence_score)} results found !\n')
    #But we only need a sentence not score from the list -> sorted_Sentence_score so let's do it
    for score ,item in sorted_Sentence_score:
        print(f'\"{item}\" with a score of {score}')
    '''
    a = [1,2,3] 
    b = [3,4,5] 
    print(sorted(zip(a ,b)))   -------------> [(1,3) ,(2,4),(3,5))]
    '''