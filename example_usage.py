from client import ReservoirSampler

def main():
    print("=== Reservoir Sampling Algorithm R ===")
    sampler = ReservoirSampler()
    stream = range(1000)
    res = sampler.sample_stream(stream, k=10)
    print("Reservoir Sample:", res)
    assert res["sample_size"] == 10
    assert res["stream_items_processed"] == 1000

    print("Reservoir Sampler verified successfully!")

if __name__ == "__main__":
    main()
