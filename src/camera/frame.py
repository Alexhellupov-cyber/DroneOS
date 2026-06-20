from dataclasses import dataclass

import numpy as np


@dataclass
class Frame:

    image: np.ndarray | None = None

    width: int = 0

    height: int = 0

    timestamp: float = 0.0