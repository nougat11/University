/*
 * The branch perdiction module with the following strategies
 *   Always Taken
 *   Always Not Taken
 *   Backward Taken, Forward Not Taken
 *   Branch Prediction Buffer with 2bit history information
 * 
 * Created by He, Hao on 2019-3-25
 */

#ifndef BRANCH_PREDICTOR_H
#define BRANCH_PREDICTOR_H

#include <cstdint>
#include <string>

const int PRED_BUF_SIZE = 4096;

class BranchPredictor {
public:
  enum Strategy {
    AT, // Always Taken
    NT, // Always Not Taken
    BTFNT, // Backward Taken, Forward Not Taken
    BPB, // Branch Prediction Buffer with 2bit history information
    RAND, // Random
    SB, //Saturating One BIt
    STB,
    PP,
    HP, //Saturating Two Bits
  } strategy;

  BranchPredictor();
  ~BranchPredictor();

  bool predict(uint32_t pc, uint32_t insttype, int64_t op1, int64_t op2,
               int64_t offset);

  // For Branch Prediction Buffer 
  void update(uint32_t pc, bool branch);

  std::string strategyName();
  
private:
  enum PredictorState {
    STRONG_TAKEN = 0, WEAK_TAKEN = 1,
    STRONG_NOT_TAKEN = 3, WEAK_NOT_TAKEN = 2,
  } predbuf[PRED_BUF_SIZE]; // initial state: WEAK_TAKEN
  enum BitState {
   NOT_TAKEN = 0, TAKEN = 1,
  } bit_state;
  enum TwoBitState {
    ST = 0, WT = 1,
    SNT = 3, WNT = 2,
  } two_bit_state;
  int psize = 200;
  int wsize = 120;
  int kTheta = static_cast<int>(1.93 * wsize + 14);
  int weightsize = 8;
  int history[120] = {-1};
  int perceptrons[200] = {1};
  int weights[200][120] = {{0}};
  int y;
  int k;
  int hs = 0;
};

#endif
