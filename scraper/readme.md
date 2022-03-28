FitnessDay = FitnessYesterday + (StressScoreDay - FitnessYesterday) * (1-e-1/42)
FatigueDay = FatigueYesterday + (StressScoreDay - FatigueYesterday) * (1-e-1/7)
FormDay = FitnessYesterday - FatigueYesterday

TrainingZone  = Transition zone, Freshness, Neutral, Optimal and Over-Training.
- +25 < Form : Transition zone. Athlete is on form. Case where athlete has an extended break. (e.g. illness, injury or end of the season).
- +5 < Form < +25 : Freshness Zone. Athlete is on form. Ready for a race or big day(s).
- -10 < Form < +5 : Neutral Zone. Zone reached typically when athlete is in a rest or recovery week. After a race or hard training period.
- -30 < Form < -10 : Optimal Training Zone. Where athlete can build an effective fitness.
- Form < -30 : Over Load Zone. Athlete is on overload or over-training phase. He should take a rest!

EffortInSeconds = data uit activity 
Weigthed Power = Strava Normalized Power = Strava Average Weigthed Watts


StressScoreDay = PowerStressScore (PSS) = (( EffortInSeconds x Weigthed Power x Intensity ) / ( FTP * 3600) ) x 100

Intensity = WeightedPower / FTP = NormalizedPower van Strava / FTP 





