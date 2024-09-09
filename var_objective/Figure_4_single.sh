echo "Running Figure 4 experiments..."

# D-CIPHER
echo "D-CIPHER"

for num_samples in 5
do
    echo "Num samples: $num_samples"
    python -m var_objective.run_var_square DrivenHarmonicOscillator 0 2.0 20 0.01 200 "NumbersRandom2" "2spline1Dtrans" 10 50 l1 lars-imp --seed 2 --num_samples $num_samples --generations 30 --exp_name "ForcedHarmonicOscillator";
done
