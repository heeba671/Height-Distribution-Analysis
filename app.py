import numpy as np
import matplotlib.pyplot as plt

# Step 1: Input heights from students
n = int(input("Enter number of students: "))

heights = []
for i in range(n):
    h = float(input(f"Enter height of student {i+1} (in cm): "))
    heights.append(h)

# Convert to numpy array for easy calculations
heights_array = np.array(heights)

# Step 2: Calculate Mean and Standard Deviation
mean_height = np.mean(heights_array)
std_dev = np.std(heights_array)

print("\n--- Results ---")
print("Mean height:", mean_height)
print("Standard Deviation:", std_dev)

# Step 3: Plot Histogram (Bell Curve Shape)
plt.hist(heights_array, bins=10, density=True)

# Step 4: Plot Normal Distribution Curve
x = np.linspace(min(heights_array), max(heights_array), 100)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(- (x - mean_height)**2 / (2 * std_dev**2))

plt.plot(x, y)

# Labels
plt.title("Height Distribution (Check for Bell Curve)")
plt.xlabel("Height (cm)")
plt.ylabel("Density")

plt.show()

# Step 5: Basic Check for Normal Distribution
if std_dev > 0:
    print("\nIf the graph looks like a symmetric bell shape,")
    print("then the data approximately follows a normal distribution.")
else:
    print("Standard deviation is 0, data is not distributed.")
