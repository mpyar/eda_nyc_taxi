Great question — choosing **mean vs. median for imputing missing values in numeric columns** depends on the **distribution of the data** and the presence of **outliers**. Let’s break it down:

---

## 📊 When to Use **Mean Imputation**
- **Best for**: Symmetric, normally distributed data (bell curve).
- **Why**: Mean represents the central tendency well when values are evenly spread.
- **Example**: Heights of adults in a population (no extreme outliers).
- **Code**:
  ```python
  df['col'] = df['col'].fillna(df['col'].mean())
  ```

---

## 📊 When to Use **Median Imputation**
- **Best for**: Skewed distributions or data with outliers.
- **Why**: Median is robust — it’s not pulled by extreme values.
- **Example**: Income data (a few very high earners skew the mean).
- **Code**:
  ```python
  df['col'] = df['col'].fillna(df['col'].median())
  ```

---

## 🔎 Quick Comparison

| Situation | Better Choice | Reason |
|-----------|---------------|--------|
| Normal distribution | **Mean** | Captures central tendency |
| Skewed distribution | **Median** | Resistant to skew |
| Outliers present | **Median** | Not influenced by extremes |
| Small dataset | **Median** | More stable with few values |
| Large dataset, no skew | **Mean** | Efficient and representative |

---

## 🚕 Example in NYC Taxi Data
- **Trip Distance**: Often skewed (many short trips, few very long trips). → Use **median**.  
- **Passenger Count**: Mostly small integers (1–2 passengers dominate). → Mode or median works better than mean.  
- **Fare Amount**: Skewed by airport trips and long rides. → Use **median**.  

---

✅ **Rule of thumb**:  
- Use **mean** when data is symmetric and clean.  
- Use **median** when data is skewed or has outliers.  

---
