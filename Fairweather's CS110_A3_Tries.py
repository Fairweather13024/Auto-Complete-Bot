#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[ ]:


NAME = ""
COLLABORATORS = ""


# ---

# # CS110 Fall 2020 - Assignment 3
# # Trie trees
# 
# **Fell free to add more cells to the ones always provided in each question to expand your answers, as needed. Make sure to refer to the [CS110 course guide](https://drive.google.com/file/d/1NUeMvAiGGMjif8IgLZjvwvwwzjBEx9Q0/view?pli=1) on the grading guidelines, namely how many HC identifications and applications you are expected to include in each assignment.**
# 
# Throughout the assignment, key **"checklist items"** you have to implement or answer are bolded, while *hints* and other interesting accompanying notes are written in italics to help you navigate the text.
# 
# If you have any questions, do not hesitate to reach out to the TAs in the Slack channel "#cs110-algo-f20", or come to one of your instructors' OHs.
# 
# ### Submission Materials
# Your assignment submission needs to include the following resources:
# 1. A PDF file must be the first resource and it will be created from the Jupyter notebook template provided in these instructions. Please make sure to use the same function names as the ones provided in the template. If your name is “Dumbledore”, your PDF should be named “Dumbledore.pdf”.
# 2. Your second resource must be a single Python/Jupyter Notebook named “Dumbledore.ipynb”. You can also submit a zip file that includes your Jupyter notebook, but please make sure to name it “Dumbledore.zip” (if your name is Dumbledore!).
# 
# ## Question 0 [#responsibility]
# 
# Take a screenshot of your CS110 dashboard on Forum where the following is visible:
# * your name.
# * your absences for the course have been set to excused up to the end of week 9 (inclusively).
# 
# This will be evidence that you have submitted acceptable pre-class and make-up work
# for a CS110 session you may have missed. Check the specific CS110 make-up and
# pre-class policies in the syllabus of the course.

# In[157]:


from IPython.display import Image
Image(filename=r"cs110 dashboard.PNG")


# ## Overview
# 
# Auto-completion functionalities are now ubiquitous in search engines, document editors, and messaging apps. How would you go about developing an algorithmic strategy to implement these computational solutions? In this assignment, you will learn about a new data structure and use it to build an auto-complete engine. Each question in the assignment guides you closer to that objective while encouraging you to contrast this novel data structure to the other ones we have discussed in class.
# 
# A [trie tree](https://en.wikipedia.org/wiki/Trie), or a prefix tree, is a common data structure that stores a set of strings in a collection of nodes so that all strings with a common prefix are found in the same branch of the tree. Each node is associated with a letter, and as you traverse down the tree, you pick up more letters, eventually forming a word. Complete words are commonly found on the leaf nodes. However, some inner nodes can also mark full words.
# 
# Let’s use an example diagram to illustrate several important features of tries:
# 
# ![tries01.png](attachment:tries01.png)
# 
# - Nodes that mark valid words are marked in yellow. Notice that while all leaves are considered valid words, only some inner nodes contain valid words, while some remain only prefixes to valid words appearing down the branch.
# 
# - The tree does not have to be balanced, and the height of different branches depends on its contents.
# 
# - In our implementation, branches never merge to show common suffixes (for example, both ANT and ART end in T, but these nodes are kept separate in their respective branches). However, this is a common first line of memory optimization for tries.
# 
# - The first node contains an empty string; it “holds the tree together.”
# 
# Your task in this assignment will be to implement a functional trie tree. You will be able to insert words into a dictionary, lookup valid and invalid words, print your dictionary in alphabetical order, and suggest appropriate suffixes like an auto-complete bot.
# 
# The assignment questions will guide you through these tasks one by one. To stay safe from breaking your own code, and to reinforce the idea of code versioning, under each new question first **copy your previous (working) code**, and only then **implement the new feature**. The code skeletons provided throughout will make this easier for you at the cost of repeating some large portions of code.

# ## Q1: Implement a trie tree [#PythonProgramming, #CodeReadability, #DataStructures]
# 
# In this question, you will write Python code that can take a set/list/tuple of strings and insert them into a trie tree and lookup whether a specific word/string is present in the trie tree.
# 
# ### Q1a: Theoretical pondering
# 
# Two main approaches to building trees, you might recall from class, are making separate Tree and Node classes, or only making a Node class. Which method do you think is a better fit for trie trees, and why? Justify your reasoning in around 100 words.

# YOUR ANSWER HERE
# 
# #### Answer
# The implementation with two classes is esecially useful for trees with invariants and properties that are identical in each node. Therefore, my assessment of this problem would not require two classes because each node is a non-unique element which may be replicated in any position throughout the tree.
# 
# Secondly, one class implementations may make it difficult to scale the code because the attributes will end up depening on each other and they may be muted erroneously. 
# 
# Lastly, intuitively, we think of the tree as an entity with nodes, hence the visualization is easier which allows us to easily ideate over more interesting trie problems that we may encounter.

# ### Q1b: Practical implementation
# 
# *However, as often happens in the life of a software engineer, the general structure of code has already been determined for you. (The reasons this commonly happens are beyond the scope of this assignment, but they could include someone having written tests for you in a [TDD environment](https://en.wikipedia.org/wiki/Test-driven_development) which have a specific structure, or the need to comply with an older codebase.)*
# 
# Specifically, **implement a Node class**, which will store the information relevant to each of the trie nodes. It doesn’t have to include any methods, but you will likely find out several attributes that are necessary for a successful implementation.
# 
# Alongside this **create a Trie class**, which will represent the tree as a whole. Upon its initiation, the Trie class will create the root Node of the trie.
# 
# For the Trie class, write **insert()** and **lookup()** methods, which will insert a word into the trie tree and look it up, respectively. Use the code skeleton below and examine the specifications of its docstrings to guide you on the details of inputs and outputs to each method.
# 
# Finally, make sure that the trie can be **initiated with a wordbank as an input**. This means that a user can create a trie and feed it an initial dictionary of words (e.g. trie = Trie(wordlist)), which will be automatically inserted into the trie upon its creation. Likely, this will mean that your __init__() has to make some calls to your insert().
# 
# Several test cases have been provided for your convenience and these include some, but not all, possible edge cases. If the implementation is correct, your code will pass all the tests. In addition, create at least **three more tests** to demonstrate that your code is working correctly and justify why such test cases are appropriate.
# 
# Use as many code cells on this as you deem necessary. The first cell with the docstrings is locked to prevent accidental deletion.

# In[173]:


# YOUR CODE HERE
class Node_Q1:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, letter = None, is_word = False):
        self.children = {}   #Every node will have an accessing point  which may store multiple other nodes
                            #I choose to use a dictionary in order to use the key to prevent duplicates, and so that I can have multiple values 
                            #The access time for teh key is also O(1) which is excellent
        self.is_word = is_word   #Attribute for if the input is a complete word
        self.letter = letter   #Attribute for the actual string in the node
        
        
class Trie_Q1:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's init are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    def __init__(self, word_list = None):
        """Creates the Trie instance, inserts initial words if provided.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node_Q1()   #Creating an empty root
        self.preparation(word_list)   #First step of inputing the words into the trie 
        
    def preparation(self, arr):
        '''Helps iterate through the training dictionary if a list is passed
        
        Parameters
        ______
        arr : array
            array of strings to be inserted into the trie
        
        '''
        for i in arr:   #We access all the words as a single entity and then pass them into the insert method
            self.insert(i)
            
        
    
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        current = self.root    #Setting the pointer
        word = word.lower()   #Convert all inputs to lowercase letters
        for i in word:  #Access the first letters in each word to check if they are in the trie
            if i not in current.children:
                current.children[i] = Node_Q1(i)   #Adding the letter to the trie as a key:value
            current = current.children[i]   #Sliding the pointer along to create a new node in
        current.is_word = True  #At the end of each iteration we have a word, hence I update the attribute

        
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        current = self.root   #Setting the pointer
        if type(word) != str:   #Checking for type edge cases
            return False
        print(current.children)
            
        for i in range(len(word)):   #Iterating over the input to check if the letters are in each subsequent trie level
            if word[i] not in current.children:
                return False
            else:
                current = current.children[word[i]]   #Moving the slider along
            
        if current.is_word == True:   #Checking if the last letter node corresponds to the word attribute
            return True
        else:
            return False  #Prefix
        


# In[174]:


# Here are several tests that have been created for you.
# Remeber that the question asks you to provide several more,
# as well as justify them.

# This is Namárië, JRRT's elvish poem written in Quenya
wordbank = "Ai! laurië lantar lassi súrinen, yéni unótimë ve rámar aldaron! Yéni ve lintë yuldar avánier mi oromardi lisse-miruvóreva Andúnë pella, Vardo tellumar nu luini yassen tintilar i eleni ómaryo airetári-lírinen. Sí man i yulma nin enquantuva? An sí Tintallë Varda Oiolossëo ve fanyar máryat Elentári ortanë, ar ilyë tier undulávë lumbulë; ar sindanóriello caita mornië i falmalinnar imbë met, ar hísië untúpa Calaciryo míri oialë. Sí vanwa ná, Rómello vanwa, Valimar! Namárië! Nai hiruvalyë Valimar. Nai elyë hiruva. Namárië!".replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace(";", "").split()

trie = Trie_Q1(wordbank)

assert trie.lookup('oiolossëo') == True  # be careful about capital letters!
assert trie.lookup('an') == True  # this is a prefix, but also a word in itself
assert trie.lookup('ele') == False  # this is a prefix, but NOT a word
assert trie.lookup('Mithrandir') == False  # not in the wordbank


# In[175]:


# YOUR NEW TESTS HERE

assert trie.lookup([0]) == False   #Edge case of wrong type
assert trie.lookup('Ai') == False   #Edge case of the cleaning functions not working
assert trie.lookup('ai!') == False
assert trie.lookup('') == False #Edge case if nothing is passed
assert trie.lookup('-') == False #Edge case if a helper character is passed


# ### Justification.
# 
# In this case, I regard the trie as a data structure that behaves like a dictionary.
# I looked at writing patterns that most people have that would violate the trie, and chose my test cases so that I could check for common problems that could arise from inputing general text as training data.
# 
# My first test case checks for type differences because the texts we use often have numerical digits.
# 
# The second and third tests were just to verify that the cleaning methods that are called after the inputs actually function. 
# 
# The last test case is for common punctuation marks that were not cleaned out because they may change the meaning of the word if they are.

# ## Q2: The computational complexity of tries [#ComplexityAnalysis, #DataStructures]
# 
# Evaluate the **computational complexity of the insert() and lookup()** methods in a trie. What are the relevant variables for runtime? You might want to consider how the height of a trie is computed to start addressing this question.  Make sure to clearly explain your reasoning.
# 
# **Compare your results to** the runtime of the same operations on **a BST**. Can you think of specific circumstances where the practical runtimes of operations supported by tries are higher than for BSTs? Explain your answer. If you believe such circumstances could be common, why would someone even bother implementing a trie tree?

# YOUR ANSWER HERE
# 
# For insertion the time complexity of the trie is $ \theta $ (n) where n is the length of the input that has been passed. This is the upper and lower bound in my case because the loops must always go through the whole string input. For searching the time complexity is O(n) as the upper bound, or $ \omega $(1) as the lower bound because if the first character does not correspond to any level 1 trie character. In the event that the input only has a prefix present, then the time complexity is O(n).
# 
# In a BST, the insert and search operartions will depend on the height of the tree, but generally we expect a time complexity of O(h) where h is the height of the tree. h may be log_2 n (If the tree has two children branches) in a balanced tree, or n in an absolutely skewed tree, leading to O(log_2 n) or O(n) in respective scenarios. 
# 
# Theoretically, if one were to train a BST on sorted inputs of strings to be added to the BST's nodes, then accessed the inputs from the middle, or they used shuffled inputs, then they could expect to have a balanced tree. The search time of such a tree would be the height of the tree which is O(log_2 n) in an AVL and RB tree whereas the trie would have a search time of O(n) where n is the length of the input. Common training data from, say a speech should have fairly randomly ordered inputs, hence the BST would be favored. However, in my trie, searching takes practically less time because the second step only accesses the correct key because of the dictionary implementation, and the likelyhood of the trie growing taller than a BST of the same input is low because word lengths are often short, hence implementing a trie with dictionaries makes the trie a good data structure for the problem.

# ## Q3: Print a dictionary in alphabetical order. [#PythonProgramming, #CodeReadability]
# 
# Recall the meaning of pre-order traversal from your previous classes. On the data structure of a trie tree, pre-order traversal corresponds to an alphabetically sorted list of the words contained within (provided that your node children are sorted alphabetically). Copy your existing code to the code skeleton cell below, and add a new method to it, **preorder_traversal()**. This will be version two of your autocomplete script.
# 
# The method should **return a list**, whose elements will be the words contained in the tree, in alphabetical order. On top of passing the provided test, write at least **three more tests**, and explain why they are appropriate.
# 
# **Approach choice:** Remember the two possible approaches to the problem, as we’ve seen at the start of the course: iterative or recursive. Depending on your trie implementation, one might be preferred over the other. **Justify your choice of approach** in a few sentences (~100 words).
# 
# Copy-paste your previous code and make adjustments to this "new version", so that you cannot break the old one :). The first cell has been locked to stop you from accidentally deleting the docstrings. Please code below.
# 
# *(Hint: If you choose a recursive approach, it might be useful to implement a helper method that is not called by the user but by preorder_traversal().)*

# Preorder traversal implementation inspired by:
# Albert Au Yeung. (2020, June 14). Implementing Trie in Python - Albert Au Yeung. Retrieved November 18, 2020, from Github.io website: https://albertauyeung.github.io/2020/06/15/python-trie.html
# 

# In[186]:


class Node_Q3:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, letter = None, is_word = False):
        self.children = {}   #Every node will have an accessing point  which may store multiple other nodes
                            #I choose to use a dictionary in order to use the key to prevent duplicates, and so that I can have multiple values 
                            #The access time for teh key is also O(1) which is excellent
        self.is_word = is_word   #Attribute for if the input is a complete word
        self.letter = letter   #Attribute for the actual string in the node
        
        
class Trie_Q3:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's init are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    def __init__(self, word_list = None):
        """Creates the Trie instance, inserts initial words if provided.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node_Q3()   #Creating an empty root
        self.preparation(word_list)   #First step of inputing the words into the trie 
        
    def preparation(self, arr):
        '''Helps iterate through the training dictionary if a list is passed
        
        Parameters
        ______
        arr : array
            array of strings to be inserted into the trie
        
        '''
        for i in arr:   #We access all the words as a single entity and then pass them into the insert method
            if type(i) != str:
                arr.delete(i)
            else:
                self.insert(i)
            
        
    
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        current = self.root    #Setting the pointer
        word = word.lower()   #Convert all inputs to lowercase letters
        for i in word:  #Access the first letters in each word to check if they are in the trie
            if i not in current.children:
                current.children[i] = Node_Q1(i)   #Adding the letter to the trie as a key:value
            current = current.children[i]   #Sliding the pointer along to create a new node in
        current.is_word = True  #At the end of each iteration we have a word, hence I update the attribute

        
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        current = self.root   #Setting the pointer
        if type(word) != str:   #Checking for type edge cases
            return False
        print(current.children)
            
        for i in range(len(word)):   #Iterating over the input to check if the letters are in each subsequent trie level
            if word[i] not in current.children:
                return False
            else:
                current = current.children[word[i]]   #Moving the slider along
            
        if current.is_word == True:   #Checking if the last letter node corresponds to the word attribute
            return True
        else:
            return False  #Prefix
        

    def preorder_traversal(self):
        """Delivers the content of the trie in alphabetical order.

        The method should both print the words out and return them in a list.
        You can create other methods if it helps you,
        but the tests should use this one.
        
        Returns
        ----------
        list
            List of strings, all words from the trie in alphabetical order.
        """
        sorted_dictionary = []   #Initializing the output array
        keys = list(self.root.children.keys())   #Accessing the first level of the tree, and sorting them in order to dictate the order of appending I use
        keys.sort()
        
        for i in keys:    #We access the first level strings and perform a depth search on them
            word_builder = self.prep(i)
            sorted_dictionary += word_builder #Receives output from the search as a letter and builds the words using the first letter
        return sorted_dictionary  
    
    def prep(self,char):
        '''Helper function that helps construct each word after each depth traversal
        
        Parameters
        ___
        char : str
                String that is the first letter of the word of interest
        Returns
        an object withthe built string
        
        '''
        self.word_builder_list = []
        node = self.root.children[char]
        self.search(node)
        return self.word_builder_list 
        
    def search(self, node, prefix = ""):
        """Searches throughthe children of every level 1 node in the trie
        
        Parameters:
            - node: the letter whose attributes we check and append
            - prefix: the word being built up
        """
        if node.is_word:   #check if the input is a word, if yes, then we return its letter to the parent
            self.word_builder_list.append(prefix + node.letter)
        #We access all teh children of the current node and traverse the path as we build the prefix
        sorted_children = list(node.children.values())
        sorted_children = sorted(sorted_children, key=lambda child: child.letter)
        
        for i in sorted_children:  #Iteratively accessing the route until the last letter is found
            self.search(i, prefix + node.letter)
 


# In[187]:


wordbank = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis pulvinar. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos. Nunc dapibus tortor vel mi dapibus sollicitudin. Etiam quis quam. Curabitur ligula sapien, pulvinar a vestibulum quis, facilisis vel sapien.".replace(",", "").replace(".", "").split()

trie = Trie_Q3(wordbank)
assert trie.preorder_traversal() == ['a','ad','adipiscing','amet','aptent','class','consectetuer','conubia','curabitur','dapibus','dolor','duis','elit','etiam','facilisis','hymenaeos','inceptos','ipsum','ligula','litora','lorem','mi','nostra','nunc','per','pulvinar','quam','quis','sapien','sit','sociosqu','sollicitudin','taciti','torquent','tortor','vel','vestibulum']


# In[194]:


# YOUR NEW TESTS HERE
#Empty input
ins = ''
trie_test = Trie_Q3(ins)

assert trie_test.preorder_traversal() == [] #Edge case for empty inputs

ins_2 = 'Another day. Another activity. Another moment to splendor'.replace(",", "").replace(".", "").split()
trie_test1 = Trie_Q3(ins_2)

#Duplicates
assert trie_test1.preorder_traversal() == ['activity', 'another', 'day', 'moment', 'splendor', 'to']

ins_3 = '911 211 321 121'.replace(",", "").replace(".", "").split()

#Recognizes numbers eg phone numbers for a directory
trie_test2 = Trie_Q3(ins_3)
assert trie_test2.preorder_traversal() == [ '121', '211', '321', '911']


# YOUR ANSWER HERE
# 
# ### Test justification
# For the first one, I considered the case that the user does not search for anything. This ensures that the program is not hard writing answers that do not exist.
# 
# In my second test case, I test whether the traversal handles duplicates, hence words that are commonly used such as 'and' and 'if' are not repeated as this may destroy the applicability of the trie for auto-complete functions.
# 
# Lastly, I expanded the possibilities of the trie to include a directory such as a phonebook. This is because addresses, phone numbers such as 911 would be wise to automplete if tehy are frequently used. I was testing if the type conditions would hold within my insert function.
# 
# 
# ### Recursion vs Iteration
# 
# I chose to use recursion so that I could have easy-to-understand, and orgaized code. This is because I implemented several helper functions for the insert method and pre_order_traversal methods. This allowed me to easily track outputs and debug effectively.
# 
# This is a tradeoff because I know that recursion in python has a small and bounded call stack which would drastically limit the number of words I can train my trie with at a time. However, this call stack can be expanded, and I can also insert inputs in batches if the size is too large by using a simple conditional and loop. Hence, I think understandable, scalable code (using recursion) is better in this instance.

# ## Q4: Find the k most common words in a speech. [#PythonProgramming, #CodeReadability]
# 
# To mathematically determine the overall connotation of a speech, you might want to compute which words are most frequently used and then run a [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis). To this end, add a method to your code, **k_most_common()** that will take as an input k, an integer, and return a list of the k most common words from the dictionary within the trie. The structure of the output list should be such that each entry is a tuple, the first element being the word and the second an integer of its frequency (see docstring if you’re confused).
# 
# To complete this exercise, you don’t have to bother with resolving ties (for example, if k = 1, but there are two most common words with the same frequency, you can return either of them), but consider it an extra challenge and let us know if you believe you managed to solve it.
# 
# The test cell below downloads and preprocesses several real-world speeches, and then runs the k-most-common word analysis of them; your code should pass the tests. As usual, add at least **three more tests**, and justify why they are relevant to your code (feel free to find more speeches to start analysing too!).
# 
# Again, copy-paste your previous code and make adjustments to this "new version". The first cell has been locked to stop you from accidentally deleting the docstrings.
# 
# Completing this question well will help you to tackle Q5!
# 
# *(Hint: This task will probably require your nodes to store more information about the frequency of words inserted into the tree. One data structure that might be very useful to tackle the problem of traversing the tree and finding most common words is heaps — you are allowed to use the heapq library or another alternative for this task.)*

# In[282]:


class Node_Q4:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, letter = None, is_word = False):
        self.children = {}   #Every node will have an accessing point  which may store multiple other nodes
                            #I choose to use a dictionary in order to use the key to prevent duplicates, and so that I can have multiple values 
                            #The access time for teh key is also O(1) which is excellent
        self.is_word = is_word   #Attribute for if the input is a complete word
        self.letter = letter   #Attribute for the actual string in the node
        self.counter = 0  #This is teh counter for the sentiment analysis
        
class Trie_Q4:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's init are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    def __init__(self, word_list = False):
        """Creates the Trie instance, inserts initial words if provided.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node_Q4()   #Creating an empty root
        self.preparation(word_list)   #First step of inputing the words into the trie 
        
    def preparation(self, arr):
        '''Helps iterate through the training dictionary if a list is passed
        
        Parameters
        ______
        arr : array
            array of strings to be inserted into the trie
        
        '''
        if type(arr) != str:
            pass
        else:
            for i in arr:   #We access all the words as a single entity and then pass them into the insert method
                if type(i) != str:
                    arr.delete(i)
                else:
                    self.insert(i)


    
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        current = self.root    #Setting the pointer
        word = word.lower()   #Convert all inputs to lowercase letters
        for i in word:  #Access the first letters in each word to check if they are in the trie
            if i not in current.children:
                current.children[i] = Node_Q4(i)   #Adding the letter to the trie as a key:value
            current = current.children[i]   #Sliding the pointer along to create a new node in
        current.is_word = True  #At the end of each iteration we have a word, hence I update the attribute
        
        current.counter += 1 
        
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        current = self.root   #Setting the pointer
        if type(word) != str:   #Checking for type edge cases
            return False
            
        for i in range(len(word)):   #Iterating over the input to check if the letters are in each subsequent trie level
            if word[i] not in current.children:
                return False
            else:
                current = current.children[word[i]]   #Moving the slider along
            
        if current.is_word == True:   #Checking if the last letter node corresponds to the word attribute
            return True
        else:
            return False  #Prefix
    
    def preorder_traversal(self):
        """Delivers the content of the trie in alphabetical order.

        The method should both print the words out and return them in a list.
        You can create other methods if it helps you,
        but the tests should use this one.
        
        Returns
        ----------
        list
            List of strings, all words from the trie in alphabetical order.
        """
        sorted_dictionary = []   #Initializing the output array
        keys = list(self.root.children.keys())   #Accessing the first level of the tree, and sorting them in order to dictate the order of appending I use
        keys.sort()
        
        for i in keys:    #We access the first level strings and perform a depth search on them
            word_builder = self.prep(i)
            sorted_dictionary += word_builder #Receives output from the search as a letter and builds the words using the first letter
        
        sorted_dictionary = sorted(sorted_dictionary, key = lambda x: x[1], reverse = True)  #This sorts the tuples in descending order for sentiment analysis
        return sorted_dictionary  
  
    def prep(self,char):
        '''Helper function that helps construct each word after each depth traversal
        
        Parameters
        ___
        char : str
                String that is the first letter of the word of interest
        Returns
        an object withthe built string
        
        '''        
        self.word_builder_list = []
        node = self.root.children[char]

        self.search(node)
        return self.word_builder_list 
      

    def search(self, node, prefix = ""):
        """Searches throughthe children of every level 1 node in the trie
        
        Parameters:
            - node: the letter whose attributes we check and append
            - prefix: the word being built up
        """
        if node.is_word:   #check if the input is a word, if yes, then we return its letter to the parent
            self.word_builder_list.append((prefix + node.letter, node.counter))
        #We access all teh children of the current node and traverse the path as we build the prefix
        sorted_children = list(node.children.values())
        sorted_children = sorted(sorted_children, key=lambda child: child.letter)
        
        for i in sorted_children:  #Iteratively accessing the route until the last letter is found
            self.search(i, prefix + node.letter)
            
            
 
    def k_most_common(self, k):
        """Finds k words inserted into the trie most often.

        You will have to tweak some properties of your existing code,
        so that it captures information about repeated insertion.

        Parameters
        ----------
        k : int
            Number of most common words to be returned.

        Returns
        ----------
        list
            List of tuples.
            
            Each tuple entry consists of the word and its frequency.
            The entries are sorted by frequency.

        Example
        -------
        >>> print(trie.k_most_common(3))
        [(‘the’, 154), (‘a’, 122), (‘i’, 122)]
        
        This means that the word ‘the’ has appeared 154 times in the inserted text.
        The second and third most common words both appeared 122 times.
        """
        #Prevents non logical access
        if k <= 0:
            return []
        #Creates a new array of all the tuples of the words and their corresponding number of appearances
        most_used_words = self.preorder_traversal()  #The list is already ordered by virtue of the number of appearances of the word
        #Ref: sorted_dictionary
        return most_used_words[:k]


# In[283]:


# Mehreen Faruqi - Black Lives Matter in Australia: https://bit.ly/CS110-Faruqi
# John F. Kennedy - The decision to go to the Moon: https://bit.ly/CS110-Kennedy
# Martin Luther King Jr. - I have a dream: https://bit.ly/CS110-King
# Greta Thunberg - UN Climate Summit message: https://bit.ly/CS110-Thunberg
# Vaclav Havel - Address to US Congress after the fall of Soviet Union: https://bit.ly/CS110-Havel

# you might have to pip install urllib before running this cell
# since you're downloading data from online, this might take a while to run
import urllib.request
speakers = ['Faruqi', 'Kennedy', 'King', 'Thunberg', 'Havel']
bad_chars = [';', ',', '.', '?', '!', '_', '[', ']', ':', '“', '”', '"', '-', '-']

for speaker in speakers:
    speech = urllib.request.urlopen(f'https://bit.ly/CS110-{speaker}')
    
    trie = Trie_Q4()

    for line in speech:
        line = line.decode(encoding = 'utf-8')
        line = filter(lambda i: i not in bad_chars, line)
        words = "".join(line).split()
        for word in words:
            trie.insert(word)
 
    if speaker == 'Faruqi':
        assert trie.k_most_common(20) == [('the', 60), ('and', 45), ('to', 39), ('in', 37), ('of', 34), ('is', 25), ('that', 22), ('this', 21), ('a', 20), ('people', 20), ('has', 14), ('are', 13), ('for', 13), ('we', 13), ('have', 12), ('racism', 12), ('black', 11), ('justice', 9), ('lives', 9), ('police', 9)]
    elif speaker == 'Kennedy':
        assert trie.k_most_common(21) == [('the', 117), ('and', 109), ('of', 93), ('to', 63), ('this', 44), ('in', 43), ('we', 43), ('a', 39), ('be', 30), ('for', 27), ('that', 27), ('as', 26), ('it', 24), ('will', 24), ('new', 22), ('space', 22), ('is', 21), ('all', 15), ('are', 15), ('have', 15), ('our', 15)]
    elif speaker == 'Havel':
        assert trie.k_most_common(22) == [('the', 34), ('of', 23), ('and', 20), ('to', 15), ('in', 13), ('a', 12), ('that', 12), ('are', 9), ('we', 9), ('have', 8), ('human', 8), ('is', 8), ('you', 8), ('as', 7), ('for', 7), ('has', 7), ('this', 7), ('be', 6), ('it', 6), ('my', 6), ('our', 6), ('world', 6)]
    elif speaker == 'King':
        assert trie.k_most_common(23) == [('the', 103), ('of', 99), ('to', 59), ('and', 54), ('a', 37), ('be', 33), ('we', 29), ('will', 27), ('that', 24), ('is', 23), ('in', 22), ('as', 20), ('freedom', 20), ('this', 20), ('from', 18), ('have', 17), ('our', 17), ('with', 16), ('i', 15), ('let', 13), ('negro', 13), ('not', 13), ('one', 13)]
    elif speaker == 'Thunberg':
        assert trie.k_most_common(24) == [('you', 22), ('the', 20), ('and', 16), ('of', 15), ('to', 14), ('are', 10), ('is', 9), ('that', 9), ('be', 8), ('not', 7), ('with', 7), ('i', 6), ('in', 6), ('us', 6), ('a', 5), ('how', 5), ('on', 5), ('we', 5), ('all', 4), ('dare', 4), ('here', 4), ('my', 4), ('people', 4), ('will', 4)]


# In[284]:


# YOUR NEW TESTS HERE

import urllib.request
speakers = ['Faruqi', 'Kennedy', 'King', 'Thunberg', 'Havel']
bad_chars = [';', ',', '.', '?', '!', '_', '[', ']', ':', '“', '”', '"', '-', '-']

for speaker in speakers:
    speech = urllib.request.urlopen(f'https://bit.ly/CS110-{speaker}')
    
    trie = Trie_Q4()

    for line in speech:
        line = line.decode(encoding = 'utf-8')
        line = filter(lambda i: i not in bad_chars, line)
        words = "".join(line).split()
        for word in words:
            trie.insert(word)
 

    if speaker == 'Faruqi':
        assert trie.k_most_common(0) == []  #Edge case

        
        
        
tries = Trie_Q4()
ins = 'He ate chicken and the next day he ate turkey'.split()

for i in ins:
    tries.insert(i)
    
assert tries.k_most_common(1) == [('ate', 2)] #Edge case of duplicates
assert tries.k_most_common(-1) == [] #Edge case for non logical input


# YOUR ANSWER HERE
# #### I resolved the ties problem
# I did this by placing my sorting code higher up hence the code accesses the tie element that is first in the dictionary. Ref: line 135
# 
# My first edge case considers the common test that the user asks for 0 assuming that it will access index 0 of the list. I cater for this by returning nothing because such logic owuld prompt the user to keep subtracting 1 from k which is unfair for non-tech users
# 
# In my second case I consider whether the methods can handle competing duplicates. This is because many word are expected to appear once or twice, and it is paramount to have logic that will handle so many conflicts.
# 
# My third test handles pesky trials to break the code and return an error, which would stop everything from executing. Instead, we prompt he user to correct their k value and not have to wait to reconstruct the trie for this to be tested again.

# ## Q5: Implement an autocomplete with a Shakespearean dictionary! [#PythonProgramming, #CodeReadability]
# 
# This is by itself the most difficult coding question of the assignment, but completing Q4 thoroughly should lay a lot of the groundwork for you already.
# 
# Your task is to create a new **autocomplete()** method for your class, which will take a string as an input, and return another string as an output. If the string is not present in the tree, the output will be the same as the input. However, if the string is present in the tree, your task is to find the most common word to which it is a prefix and return that word instead (this can still turn out to be itself).
# 
# To make the task more interesting, use the test cell code to download and parse “The Complete Works of William Shakespeare”, and insert them into a trie. Your autocomplete should then pass the following tests. As usual, add at least **three more test cases**, and explain why they are appropriate (you can use input other than Shakespeare for them).
# 
# Make sure to include a minimum **100 word-summary critically evaluating** your autocomplete engine.
# 
# *(Hint: Again, depending on how you choose to implement it, your autocomplete() might make calls to other helper methods. However, make sure that autocomplete() is the method exposed to the user in order to pass the tests.)*
# 
# *This is a thoroughly frequentist approach to the problem, which is not the only method, and in many cases not the ideal method. However, if you were tasked with implementing something like [this](https://jqueryui.com/autocomplete/) or [this](https://xdsoft.net/jqplugins/autocomplete/), it might just be enough, so let’s give it a go. Good luck!*

# In[269]:


class Node_Q5:
    """This class represents one node of a trie tree.
    
    Parameters
    ----------
    The parameters for the Node class are not predetermined.
    However, you will likely need to create one or more of them.
    """

    def __init__(self, letter = None, is_word = False):
        self.children = {}   #Every node will have an accessing point  which may store multiple other nodes
                            #I choose to use a dictionary in order to use the key to prevent duplicates, and so that I can have multiple values 
                            #The access time for teh key is also O(1) which is excellent
        self.is_word = is_word   #Attribute for if the input is a complete word
        self.letter = letter   #Attribute for the actual string in the node
        self.counter = 0  #This is teh counter for the sentiment analysis
        
class Trie_Q5:
    """This class represents the entirety of a trie tree.
    
    Parameters
    ----------
    The parameters for Trie's init are not predetermined.
    However, you will likely need one or more of them.    
    
    Methods
    -------
    insert(self, word)
        Inserts a word into the trie, creating nodes as required.
    lookup(self, word)
        Determines whether a given word is present in the trie.
    """
    def __init__(self, word_list = False):
        """Creates the Trie instance, inserts initial words if provided.
        
        Parameters
        ----------
        word_list : list
            List of strings to be inserted into the trie upon creation.
        """
        self.root = Node_Q5()   #Creating an empty root
        self.preparation(word_list)   #First step of inputing the words into the trie 
        
    def preparation(self, arr):
        '''Helps iterate through the training dictionary if a list is passed
        
        Parameters
        ______
        arr : array
            array of strings to be inserted into the trie
        
        '''
        if type(arr) != str:
            pass
        else:
            for i in arr:   #We access all the words as a single entity and then pass them into the insert method
                if type(i) != str:
                    arr.delete(i)
                else:
                    self.insert(i)


    
    def insert(self, word):
        """Inserts a word into the trie, creating missing nodes on the go.
        
        Parameters
        ----------
        word : str
            The word to be inserted into the trie.
        """
        current = self.root    #Setting the pointer
        word = word.lower()   #Convert all inputs to lowercase letters
        for i in word:  #Access the first letters in each word to check if they are in the trie
            if i not in current.children:
                current.children[i] = Node_Q4(i)   #Adding the letter to the trie as a key:value
            current = current.children[i]   #Sliding the pointer along to create a new node in
        current.is_word = True  #At the end of each iteration we have a word, hence I update the attribute
        
        current.counter += 1 
        
    def lookup(self, word):
        """Determines whether a given word is present in the trie.
        
        Parameters
        ----------
        word : str
            The word to be looked-up in the trie.
            
        Returns
        -------
        bool
            True if the word is present in trie; False otherwise.
            
        Notes
        -----
        Your trie should ignore whether a word is capitalized.
        E.g. trie.insert('Prague') should lead to trie.lookup('prague') = True
        """
        current = self.root   #Setting the pointer
        if type(word) != str:   #Checking for type edge cases
            return False
            
        for i in range(len(word)):   #Iterating over the input to check if the letters are in each subsequent trie level
            if word[i] not in current.children:
                return False
            else:
                current = current.children[word[i]]   #Moving the slider along
            
        if current.is_word == True:   #Checking if the last letter node corresponds to the word attribute
            return True
        else:
            return False  #Prefix
    
    def preorder_traversal(self):
        """Delivers the content of the trie in alphabetical order.

        The method should both print the words out and return them in a list.
        You can create other methods if it helps you,
        but the tests should use this one.
        
        Returns
        ----------
        list
            List of strings, all words from the trie in alphabetical order.
        """
        sorted_dictionary = []   #Initializing the output array
        keys = list(self.root.children.keys())   #Accessing the first level of the tree, and sorting them in order to dictate the order of appending I use
        keys.sort()
        
        for i in keys:    #We access the first level strings and perform a depth search on them
            word_builder = self.prep(i)
            sorted_dictionary += word_builder #Receives output from the search as a letter and builds the words using the first letter
        
        sorted_dictionary = sorted(sorted_dictionary, key = lambda x: x[1], reverse = True)  #This sorts the tuples in descending order for sentiment analysis
        return sorted_dictionary  
  
    def prep(self, char):
        '''Helper function that helps construct each word after each depth traversal
        
        Parameters
        ___
        char : str
                String that is the first letter of the word of interest
        Returns
        an object withthe built string
        
        '''        
        self.word_builder_list = []
        node = self.root.children[char]

        self.search(node)
        return self.word_builder_list 
      

    def search(self, node, prefix = ""):
        """Searches throughthe children of every level 1 node in the trie
        
        Parameters:
            - node: the letter whose attributes we check and append
            - prefix: the word being built up
        """
        if node.is_word:   #check if the input is a word, if yes, then we return its letter to the parent
            self.word_builder_list.append((prefix + node.letter, node.counter))
        #We access all teh children of the current node and traverse the path as we build the prefix
        sorted_children = list(node.children.values())
        sorted_children = sorted(sorted_children, key=lambda child: child.letter)
        
        for i in sorted_children:  #Iteratively accessing the route until the last letter is found
            self.search(i, prefix + node.letter)
            
            
 
    def k_most_common(self, k):
        """Finds k words inserted into the trie most often.

        You will have to tweak some properties of your existing code,
        so that it captures information about repeated insertion.

        Parameters
        ----------
        k : int
            Number of most common words to be returned.

        Returns
        ----------
        list
            List of tuples.
            
            Each tuple entry consists of the word and its frequency.
            The entries are sorted by frequency.

        Example
        -------
        >>> print(trie.k_most_common(3))
        [(‘the’, 154), (‘a’, 122), (‘i’, 122)]
        
        This means that the word ‘the’ has appeared 154 times in the inserted text.
        The second and third most common words both appeared 122 times.
        """
        #Prevents non logical access
        if k <= 0:
            return []
        #Creates a new array of all the tuples of the words and their corresponding number of appearances
        most_used_words = self.preorder_traversal()  #The list is already ordered by virtue of the number of appearances of the word
        #Ref: sorted_dictionary
        return most_used_words[:k]
    
    def autocomplete(self,prefix):
        """Finds the most common word with the given prefix.

        You might want to reuse some functionality or ideas from Q4.

        Parameters
        ----------
        prefix : str
            The word part to be “autocompleted”.

        Returns
        ----------
        str
            The complete, most common word with the given prefix.
            
            The return value is equal to prefix if there is no valid word in the trie.
            The return value is also equal to prefix if prefix is the most common word.
        """
        if len(prefix) == 0:
            return False
            
        output = [] 
        suggested_words = []
        word_list = self.preorder_traversal()

        prefix_as_list = list(prefix)
        
        if len(prefix) == 0:
            return False

        for tuples in word_list:      #Acessing the words in each tuple to compare with the prefixes
            word_as_list = list(tuples[0])

            for i in range(len(prefix)):
                if word_as_list[:len(prefix)] == prefix_as_list:  #Comparison of teh input with the words in the trie that may be compatible
                     output.append(tuples)   #Storing the successfully scanned prefix word candidates
                        
        suggested_words = output[0][0] 

        #Return the full word that matches the prefix
        return suggested_words


# In[270]:


import urllib.request
response = urllib.request.urlopen('http://bit.ly/CS110-Shakespeare')
bad_chars = [';', ',', '.', '?', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', '[', ']']

trieSH = Trie_Q5()

for line in response:
    line = line.decode(encoding = 'utf-8')
    line = filter(lambda i: i not in bad_chars, line)
    words = "".join(line).split()
    for word in words:
        trieSH.insert(word)

assert trieSH.autocomplete('hist') == 'history'
assert trieSH.autocomplete('en') == 'enter'
assert trieSH.autocomplete('cae') == 'caesar'
assert trieSH.autocomplete('gen') == 'gentleman'
assert trieSH.autocomplete('pen') == 'pen'
assert trieSH.autocomplete('tho') == 'thou'
assert trieSH.autocomplete('pent') == 'pentapolis'
assert trieSH.autocomplete('petr') == 'petruchio'


# In[281]:


# YOUR NEW TESTS HERE
word = 'ans and ant anyway anywhere anywhere anything'.split()
for i in word:
    trieSH.insert(i)

assert trieSH.autocomplete('anyw') == 'anywhere' #Checking if the sentiment still applies

assert trieSH.autocomplete('an') == 'and' #Ensuring that the duplicate prefixes are sorted

assert trieSH.autocomplete('anywhere') ==  'anywhere'  #Ensure that is_word is not interfering


# YOUR ANSWER HERE
# ### Test Cases
# 
# My first test case ensures that the first and foremost matter of consideration is that the sentiment (prefix frequency) applies to all prefixes passed. This means that, based on the traning data, the user will receive the most relevant suggestion based on their most used word with that prefix. This is what makes an autocomplete bot worthwhile.
# 
# My second test case evaluates if the tie breaker property still works. This directly relates to the sentiment problem because the autocomplete bot must have a way of suggesting relevant output in the event of a tie.
# 
# Lastly, I test whether passing a full word would disrupt the auto complete bot because we expect it either to have somehow retained its node property 'is_word' or the code does not loop to the end of the word.
# 
# ### Evaluating my autocomplete bot
# 
# Pros - 
# 
# My bot is very difficult to crash once it has been trained. I have included checks in order to limit its vulnerability to iteration, type and name errors which would cause the code to stop working.
# 
# My bot operates on real world standards that one expects from an auto complete engine such as: it can resolve ties, and it assesses sentiment. 
# 
# I make the code easy to understand because I use previously created methods to build new functionalities instead of just creating everything from scratch which may be easier for problems such as the auto complete method. 
# 
# Short code - I have tried to shorten my code, and be pythonic too because it helps maintain logic flows in the mind of the reader. This makes my code scalable. 
# 
# Implementing dictionaries to contain my node classes ensures that we can access the keys with O(1) time instead of applying a breadth first search for every node that has multiple children in the next level. This saves us a lot of trainig time and allows us to use large training sets without compromising on training time.
# 
# Cons - 
# 
# I seem to sort the inputs often, which limits the training time of my bot to a lower bound of O(n log n) which is not superb (if I am traversing down). A smarter implementation, with more time, would involve accessing the first element of the word that I am passing as input and mapping that to a dictionary key for which you can access all words with that starting letter as the dictionary value. This would have an upper bound of O(n).
# 
# Also, I cannot handle input that the trie was not trained with. In the real world, I would have implemented an option to add the input into the trie for future access.
# 
# Lastly, I cannot help a user who has typos. Even though I tried to make my bot as useful as possible, it cannot handle typos. To solve this I would have to remove the typo element from the correct prefix and pass all the suggested words of the shorter prefix instead. This would mean introducing another conditional within the auto complete loop. However, when I tried this, I ran out of time trying to debug the code.
# 
# 

# ## HCs
# 
# #### #variables 
# For example, in the implementation of the trie data structure, I needed to understand what attributes were necessary for a fully functional trie as well as what attributes shall be manipulated within the node classes. Keeping #variables in mind necessitated that I track concept flows through psuedocode in order to evaluate the efficacy of implementing the tries with certain attributes. Also, I learnt how I could assign object variables using the self. variable method in order for them to be accessed throughout the class methods and be updated on the go. This was particularly useful for creating lists for the k_most_common problem. Lastly, my choice of data structure manipulation within the trie was informed by how the inputs would be written within the data structure which would vary if I used lists versus dictionaries.
# 
# 
# #### #critique
# When I applied this HC, I used it to inform my approach for the code, critically engaging with and assessing methods that would present different strengths and limitations under varying conditions. Specifically here, I evaluated the local problem of immediate limitation of understanding all dictionary methods versus using arrays which were within my comfort zone. While it may look like coding dictionaries is more difficult because of having more operations to implement within the class, dictionaries offered significant advantages over arrays. In the event of needing to scale the code, dictionaries made more sense than arrays. Scaling arrays would involve n-arrays and would make it difficult to know which array the code is considering, but with dictionaries, the key eliminates that and allows for more scalable code. Additionally, while evaluating the recursive versus iterative approaches, I critically considered the impact of the nature of the input in my toolbox of potential solutions for implementation. Thus, I concluded that an iterative approach to a pre-order traversal could have proven more limiting in the event that I had to implement more functionalities. Therefore, I devised a potential fallback solution for the limitations of recursion. Critically identifying this allowed me to produce a stronger assignment while fostering deeper engagement along the way. 
# 
# 
# #### #designthinking 
# I empathized with the user who would train or use a trie, and I collected information about how we train and maintain our dictionaries as well as how to implement code that can scale to add more interdependent methods. Therefore, in addition to the thorough comments, I included several conditions which eliminated erroneous inputs which were verified by my test cases and I also foresaw potential limitations of my insert function, making it such that the function accommodates for whatever string inputs the user may innocently pass, be it an array of multiple words, a single word or a blank. 
# In the iteration component of #designthinking, I iterated over my codes, including several lambda functions to replace loops which were unnecessary and cumbersome and which only performed simple tasks. This made my code much more readable as seen in my search method after verifying my original loops actually worked and my control flows much more understandable which also touches on #organization.
# 
# 
# #### #audience
# I considered the real word situations where an autocomplete bot is found. Often the user has particular patterns of writing which heavily rely on the bot. For example, not letting the bot complete words for you, typos and most relevant suggested words. I then tailored my test cases to accomodate for the average user because we cannot discriminate.
# 
# When writing my code, I thought about what conventions developers care about and i applied the #codereadability LO to inform my choice of mthod names, variable names and the organization of my logic (making it as linear as possible without co-dependencies and super methods). I aso implemented helper functions that did one thing well and briefly to allow for scalability and ambidexterity of the methods. Therefore, if another developer were to use my code for their project, they would have many tools to build on top of which are simple and stable.

# In[ ]:




