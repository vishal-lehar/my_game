class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0
    
    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins. Must be between 0 and 10.")
            
        self.rolls.append(pins)
    
    def _is_strike(self, roll_index):
        return roll_index < len(self.rolls) and self.rolls[roll_index] == 10
    
    def _is_spare(self, roll_index):
        return (roll_index + 1 < len(self.rolls) and 
                self.rolls[roll_index] + self.rolls[roll_index + 1] == 10)
    
    def _strike_bonus(self, roll_index):
        bonus = 0
        if roll_index + 1 < len(self.rolls):
            bonus += self.rolls[roll_index + 1]
            if roll_index + 2 < len(self.rolls):
                bonus += self.rolls[roll_index + 2]
        return bonus
    
    def _spare_bonus(self, roll_index):
        bonus = 0
        if roll_index + 2 < len(self.rolls):
            bonus = self.rolls[roll_index + 2]
        return bonus
    
    def _frame_score(self, roll_index):
        score = 0
        if roll_index < len(self.rolls):
            score += self.rolls[roll_index]
            if roll_index + 1 < len(self.rolls):
                score += self.rolls[roll_index + 1]
        return score
    
    def _get_min_rolls_needed(self):
        if not self.rolls:
            return 12  # Minimum rolls needed if all strikes
            
        roll_index = 0
        for frame in range(9):  # First 9 frames
            if self._is_strike(roll_index):
                roll_index += 1
            else:
                roll_index += 2
                
        # For the 10th frame
        if len(self.rolls) <= roll_index:
            return 12  # Default minimum if we don't have enough data
            
        # 10th frame logic
        if self._is_strike(roll_index):
            return roll_index + 3  # Strike in 10th frame allows 2 more rolls
        elif self._is_spare(roll_index):
            return roll_index + 3  # Spare in 10th frame allows 1 more roll
        else:
            return roll_index + 2  # Regular 10th frame
        
    def score(self):
        if len(self.rolls) < self._get_min_rolls_needed():
            raise ValueError("Game is not complete. Cannot calculate final score.")
            
        score = 0
        roll_index = 0

        for frame in range(10):
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self._frame_score(roll_index)
                roll_index += 2
                
        return score