class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      new_word = "" 

      if len(word1) >= len(word2):
          word_len = len(word1)
      else:
          word_len = len(word2)

      for index in range(word_len):

          if index+1 <= len(word1):
              new_word = new_word + word1[index]
              
          if index+1 <= len(word2): 
              new_word = new_word + word2[index]
              
      return new_word
          
        
