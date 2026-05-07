
---

## 🛠️ Steps to Create a New Conda Environment

1. **Open your terminal / command prompt**  
   Make sure `conda` is installed and accessible (`conda --version` should return a version number).

2. **Create the environment**  
   Use the `conda create` command with a name and optional Python version:
   ```bash
   conda create --name nyctaxi python=3.10
   ```
   - `nyctaxi` → name of your environment (choose any name).
   - `python=3.9` → optional, specifies Python version. If omitted, it uses the default.

3. **Activate the environment**  
   ```bash
   conda activate nyctaxi
   ```
   Now your prompt will show `(myenv)` at the start, meaning you’re inside that environment.

4. **Install packages**  
   Add packages as needed:
   ```bash
   conda install numpy==1.26.4
   conda install pandas==2.2.2
   conda install matplotlib==3.10.0
   conda install seaborn==0.13.2
   ```

5. **Deactivate when done**  
   ```bash
   conda deactivate
   ```

---

## 📌 Quick Notes
- Each environment is isolated, so packages installed in one don’t affect others.
- You can list all environments with:
  ```bash
  conda env list
  ```
- To remove an environment:
  ```bash
  conda remove --name myenv --all
  ```

---

