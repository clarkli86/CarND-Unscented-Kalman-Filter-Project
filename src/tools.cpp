#include "tools.h"

using Eigen::VectorXd;
using std::vector;

Tools::Tools() {}

Tools::~Tools() {}

VectorXd Tools::CalculateRMSE(const vector<VectorXd> &estimations,
                              const vector<VectorXd> &ground_truth) {
  /**
   * TODO: Calculate the RMSE here.
   */
  /// FIXME: deduce type from parameters
  auto rmse = VectorXd(4);
  rmse << 0, 0, 0, 0;
  // accumulate squared residuals
  for (unsigned int i=0; i < estimations.size(); ++i) {
    VectorXd residual = estimations[i] - ground_truth[i];

    // coefficient-wise multiplication
    residual = residual.array()*residual.array();
    rmse += residual;
  }

  // calculate the mean
  rmse = rmse/estimations.size();

  // calculate the squared root
  rmse = rmse.array().sqrt();

  return rmse;
}
