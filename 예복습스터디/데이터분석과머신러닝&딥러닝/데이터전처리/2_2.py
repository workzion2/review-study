"""
1. **결측값 분석**
   - Titanic 데이터의 결측값 시각화
   - 각 열별 결측값 개수와 비율 계산
   - Age 열: 177개 결측 (19.9%)
   - Cabin 열: 687개 결측 (77.1%)
2. **전략 1: 삭제(Deletion)**
   - `df.dropna(subset=['age'])` 사용
   - 891행 → 714행 (177행 삭제)
   - 데이터 손실률: 19.9%
   - 장점: 데이터 품질 유지
   - 단점: 정보 손실
3. **전략 2: 대체(Imputation) - 통계값 사용**
   - 평균값 대체: `age.fillna(age.mean())`
   - 중앙값 대체: `age.fillna(age.median())`
   - 최빈값 대체: `age.fillna(age.mode()[0])`
   - 장점: 데이터 크기 유지
   - 단점: 분포 왜곡 가능
   """
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")
#EDA
# 시각화
titanic_null = pd.DataFrame(df.isnull().sum())
# 결측값 개수와 비율 계산(결측값/ 전체 row)
tramp = df.isnull().sum() / len(df)
#결측 갯수
age_null = df['age'].isnull().sum() 
cabin_null = df['deck'].isnull().sum()
# 비율
age_q = age_null/ len(df)*100
cabin_q = cabin_null/ len(df)*100


#feature enginering
titanic_a= df.dropna(subset=['age'])
# 결측치 대체
df = age.fillna(age.mean())#deck, age, embarked
fillna(age.median())
fillna(age.mode()[0])


if __name__ == "__main__":
    print(titanic_null)
    print(tramp)
    print(f"나이 결측치 {age_null}")
    print(f"cabin 결측치 {cabin_null}")
    print(f"age 열 :{age_q}")
    print(f"Cabin 열:{cabin_q}")