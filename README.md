# 🌧️ Raining Pi! (Monte Carlo Simulation) 🎯

An interactive **Streamlit** application designed to explain the Monte Carlo method and the importance of Big Data to elementary and middle school students. 
Created by the Machine Learning student team at **Politecnico di Torino (PoliTo)** for **Pi Day**.

## 🚀 What is this project?

The app estimates the value of Pi ($\pi$) by simulating the random dropping of "paint drops" (points) inside a square that contains an inscribed circle. 
It is a highly visual and fun way to introduce two key Data Science concepts to younger audiences:
1. **The Law of Large Numbers**: with few data points (few drops), the error margin is huge; as the amount of data increases, the approximation becomes incredibly precise.
2. **Statistical Sampling**: how randomness can be used to solve complex mathematical problems.

## 🛠️ Requirements and Installation

This project uses [uv](https://github.com/astral-sh/uv) for lightning-fast Python package and virtual environment management.

1. Clone the repository or download the project folder.
2. Make sure you have `uv` installed on your system.
3. Create the virtual environment and install the dependencies:

```bash
uv venv
uv pip install streamlit numpy matplotlib
```

# 🧮 The Math Behind the Magic: Monte Carlo Method

The Monte Carlo method is a clever statistical technique that uses **randomness and probability** to solve complex mathematical problems. Here is how we use it to calculate Pi ($\pi$) without relying on complex geometry.

## 1. The Geometry

Imagine a square target. Inside this square, we draw the largest possible circle (an inscribed circle).
* Let the radius of the circle be $r = 1$.
* The side length of the square will be $2$ (since it spans the full diameter, from $-1$ to $1$).

Now, let's compare their areas:
* **Area of the square:** $2 \times 2 = 4$
* **Area of the circle:** $\pi \times r^2 = \pi \times 1^2 = \pi$



## 2. The Probability

If we randomly drop paint inside the square, what is the chance that a drop will land inside the circle? 

Assuming the drops are perfectly random, the probability ($P$) is simply the ratio of the two areas:
$$P = \frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi}{4}$$

## 3. The Code Algorithm

To simulate this on a computer, we use a standard $X, Y$ coordinate system with the center at $(0,0)$. 

1. We generate random $x$ and $y$ coordinates between $-1$ and $1$.
2. To check if a random point has landed inside the circle, we use the Pythagorean theorem to find its distance from the center. A point is inside the circle if:
$$x^2 + y^2 \le 1$$

## 4. Calculating Pi

As we drop thousands of random points, we keep track of where they land. Thanks to the **Law of Large Numbers**, the ratio of points that land inside the circle to the total number of points dropped will naturally converge to our probability $P$.

$$\frac{\text{Points inside}}{\text{Total points}} \approx \frac{\pi}{4}$$

To finally isolate and reveal Pi, we just multiply that ratio by 4:
$$\pi \approx 4 \times \left( \frac{\text{Points inside}}{\text{Total points}} \right)$$

The more points you generate, the more the chaos averages out, and the more accurate your estimation of Pi becomes!
