def wordCount(t):
    wordDict = {}
    file = open(t, "r")
        # Iterate through each line in the file
    for line_num, line in enumerate(file, start=1):
        # Split the line into words
        words = line.split()
        
        # Iterate through each word in the line
        for word in words:
            # Remove punctuation and convert to lowercase for uniformity
            word = word.strip('.,?!;:').lower()
            
            # If the word is already in the dictionary, append the line number
            if word in wordDict:
                if line_num not in wordDict[word]:
                    wordDict[word].append(line_num)
            # If the word is not in the dictionary, add it with the line number
            else:
                wordDict[word] = [line_num]
    return wordDict

print(wordCount("words.txt"))
