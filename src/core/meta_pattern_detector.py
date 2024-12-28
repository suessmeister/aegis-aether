class MetaPatternDetector:
    def __init__(self):
        self.patterns = []

    def detect(self, data):
        """Detect meta-patterns in incoming data."""
        print("Analyzing data for patterns...")
        if "pattern" in data:
            self.patterns.append(data)
            print(f"Pattern detected: {data}")
            return {"pattern": data}
        return None

    def get_detected_patterns(self):
        """Return all detected patterns."""
        return self.patterns