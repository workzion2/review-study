"""
선형 회귀 모델을 구축하고 성능을 평가합니다.

**📋 상세 지시사항:**

1. **데이터 준비**
   - California Housing 데이터 로드
   - 특성: 위도, 경도, 주택 연한, 방 수, 침실 수, 인구, 가구당 인원, 중앙값
   - 타겟: 중앙 주택 가격

2. **데이터 분할**
   - 훈련 데이터 80%, 테스트 데이터 20%
   - `train_test_split()` 사용

3. **모델 구축 및 학습**
   - `LinearRegression()` 객체 생성
   - `fit()` 메서드로 훈련
   - 회귀 계수 확인

4. **예측 및 평가**
   - MSE (Mean Squared Error): $\frac{1}{n}\sum(y - \hat{y})^2$
   - RMSE (Root Mean Squared Error): $\sqrt{MSE}$
   - R² (결정 계수): 모델 설명력 (0 ~ 1)

5. **결과 시각화**
   - 실제값 vs 예측값 산점도
   - 잔차 플롯
   """

from sklearn.datasets import fetch_california_housing

#California Housing 데이터 로드
housing = fetch_california_housing()
#   - 특성: 위도, 경도, 주택 연한, 방 수, 침실 수, 인구, 가구당 인원, 중앙값
#   - 타겟: 중앙 주택 가격
print(f"데이터 형태: {housing.data.shape}")
print(f"특성명: {housing.feature_names}")
print(f"타겟 설명: {housing.DESCR[:200]}...")


if __name__ == "__main__":
   print("lolo")