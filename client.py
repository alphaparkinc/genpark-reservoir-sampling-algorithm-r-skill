import random

class ReservoirSampler:
    """Reservoir Sampling (Algorithm R)."""
    def sample_stream(self, stream_iterator, k: int) -> dict:
        reservoir = []
        count = 0
        for item in stream_iterator:
            if count < k:
                reservoir.append(item)
            else:
                j = random.randint(0, count)
                if j < k:
                    reservoir[j] = item
            count += 1

        return {
            "stream_items_processed": count,
            "sample_size": len(reservoir),
            "sample": reservoir
        }
