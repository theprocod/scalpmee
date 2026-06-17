class SetupRanker:
    @staticmethod
    def rank_setup(trend_alignment: int, liquidity_confirmation: int, session_confirmation: int, volume_confirmation: int, risk_reward_confirmation: int) -> str:
        score = trend_alignment + liquidity_confirmation + session_confirmation + volume_confirmation + risk_reward_confirmation
        
        if score >= 9:
            return "A+ Setup (Score: 9+/10)"
        elif score >= 8:
            return "A Setup (Score: 8/10)"
        elif score >= 6:
            return "B Setup (Score: 6-7/10)"
        elif score >= 4:
            return "C Setup (Score: 4-5/10)"
        else:
            return "Invalid Setup"
