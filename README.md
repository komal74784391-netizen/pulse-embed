# pulse-embed

Implementation and evaluation code for **Pulse Encoders for Irregular Clinical Time Series**, published in JEMS 2025.

## Repository contents

- `src/` — pulse encoder, irregular-sampling layers, and training utilities
- `experiments/` — training and evaluation drivers
- `configs/` — experiment configuration used for the JEMS 2025 results
- `results/` — benchmark outputs reported in the paper
- `cli_interface.json` — machine-readable interface of the encoding CLI

## Quick start

```bash
pip install -r requirements.txt
python experiments/train_pulse.py --config configs/jems2025.yaml
```

## Citation

> A. Diaz, S. Halvorsen. Pulse Encoders for Irregular Clinical Time Series. JEMS 2025.
