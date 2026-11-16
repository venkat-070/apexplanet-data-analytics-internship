# Task 4: Statistical Hypothesis Testing Results
**Intern:** Venkata Vedhadri Marisetti (23981A44Y9)  
**Organization:** ApexPlanet Software Pvt. Ltd.  
**Academic Guide:** Md Imam Khader Shariff, Assistant Professor  
**Significance Level:** $\alpha = 0.05$ (95% Confidence)  

---

## Hypothesis Test 1: Promotional Discount Impact on Net Profitability
* **Null Hypothesis ($H_0$):** Mean profit of low discount transactions ($\le 10\%$) is equal to or less than high discount transactions ($> 10\%$) ($\mu_{low} \le \mu_{high}$).
* **Alternative Hypothesis ($H_1$):** High discount transactions significantly erode net profit per transaction ($\mu_{low} > \mu_{high}$).
* **Sample Sizes:** $n_{low} = 3,771$, $n_{high} = 1,743$
* **Descriptive Stats:** Low Discount Mean = $211.11 (SD = 354.32), High Discount Mean = $63.95 (SD = 183.73)
* **Test Statistics:**
  - Welch's $t$-statistic: **20.2793** (Degrees of Freedom: robust Welch-Satterthwaite)
  - Parametric $p$-value: **3.3094e-88**
  - Mann-Whitney $U$-statistic: **4547979.0**, $p$-value: **1.3642e-116**
  - Effect Size (Cohen's $d$): **0.474** (Medium-to-Large practical impact)
  - 95% Confidence Interval for $(\mu_{low} - \mu_{high})$: **[$132.94, $161.38]**
* **Conclusion:** REJECT NULL HYPOTHESIS (H0). Promotional discounts above 10% statistically and practically degrade operating profit margins.

---

## Hypothesis Test 2: Regional Sales Revenue Uniformity
* **Null Hypothesis ($H_0$):** Mean order sales are identical across all operating regions ($\mu_{East} = \mu_{West} = \mu_{Central} = \mu_{South} = \mu_{North}$).
* **Alternative Hypothesis ($H_1$):** At least one geographic region exhibits significantly different transaction revenues.
* **Test Statistics:**
  - One-Way ANOVA $F$-statistic: **1.3928**, $p$-value: **0.2337**
  - Kruskal-Wallis Non-Parametric $H$: **6.4057**, $p$-value: **0.1708**
* **Conclusion:** FAIL TO REJECT H0. Geographic regions perform consistently on per-order basket sizes, indicating unified nationwide catalog demand.

---

## Hypothesis Test 3: Segment Independence across Product Categories
* **Null Hypothesis ($H_0$):** Customer segment (Consumer, Corporate, Home Office) is independent of Product Category selection.
* **Alternative Hypothesis ($H_1$):** Customer segment and product category preferences are statistically dependent.
* **Test Statistics:**
  - Pearson's $\chi^2$-statistic: **4.7551**, Degrees of Freedom: **4**
  - Asymptotic $p$-value: **0.3134**
  - Cramer's $V$: **0.0208**
* **Conclusion:** FAIL TO REJECT H0. Cross-category distribution is consistent across client enterprise segments, supporting unified merchandising.
