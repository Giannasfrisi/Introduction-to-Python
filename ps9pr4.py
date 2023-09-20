#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """Represents an intelligent computer player in the connect four game"""
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        self.islegal = True
        
    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        
        s = ''
        if  self.checker == 'X':
            s += 'Player X '
        else:
            s += 'Player O '
            
        if self.tiebreak == 'LEFT':
            s += '(LEFT, '           
        elif self.tiebreak == 'RIGHT':
            s += '(RIGHT, '
        else:
            s += '(RANDOM, '
            
        s += str(self.lookahead) + ')'
        return s
        
    def max_score_column(self, scores):
        """that takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score"""
        
        possible_col = []
        max_score = max(scores)
        for i in range(len(scores)):
            if scores[i] == max_score:
                possible_col += [i]
        
        if len(possible_col) >= 1:
            if self.tiebreak == 'LEFT':
                col = possible_col[0]
                return col
            elif self.tiebreak == 'RIGHT':
                col = possible_col[-1]
                return col
            else:
                col = random.choice(possible_col)
                return col
        
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores for the columns in b"""
        
        scores = [50] * b.width
        for col in range(b.width):
             if b.can_add_to(col) == False:
                 scores[col] = -1
             elif b.is_win_for(self.checker) == True:
                 scores[col] = 100
             elif b.is_win_for(self.opponent_checker()) == True:
                 scores[col] = 0 
             elif self.lookahead == 0:
                scores[col] = 50
             else:
                b.add_checker(self.checker, col) 
                opponent_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                
                opp_scores = opponent_player.scores_for(b)
                
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
               
                b.remove_checker(col)
        
        return scores
        
        
    def next_move(self, b):
        """return the called AIPlayer‘s judgment of its best possible move"""
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
        
        
        
        
        
        
        
        
        
        
        
        
        
        