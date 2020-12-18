/*
 * Created by He, Hao on 2019-3-25
 */

#include "BranchPredictor.h"
#include "Debug.h"

BranchPredictor::BranchPredictor() {
  for (int i = 0; i < PRED_BUF_SIZE; ++i) {
    this->predbuf[i] = WEAK_TAKEN;
  }
  this->bit_state = NOT_TAKEN;
  this->two_bit_state = WT;
}

BranchPredictor::~BranchPredictor() {}

bool BranchPredictor::predict(uint32_t pc, uint32_t insttype, int64_t op1,
                              int64_t op2, int64_t offset) {
  switch (this->strategy) {
  case NT:
    return false;
  case AT:
    return true;
  case RAND:
    return (rand() % 2 == 1);
  case BTFNT: {
    if (offset >= 0) {
      return false;
    } else {
      return true;
    }
  }
  break;
  case PP:{
    this-> k = pc % this->psize;
    this->y = this->perceptrons[k];
    for (int i = 0; i < this->wsize; ++i){
      int h = i % this->wsize;
      y += this->weights[k][i] * history[h];
      
    }
    if (this->y >=0) return true;
    else return false;
}
  break;
  case HP: {
    bool a, b, c;
    int ct = 0, cf = 0;
    a = (offset >= 0) ? false : true;
    PredictorState state = this->predbuf[pc % PRED_BUF_SIZE];
    if (state == STRONG_TAKEN || state == WEAK_TAKEN) {
      b = true;
    } else if (state == STRONG_NOT_TAKEN || state == WEAK_NOT_TAKEN) {
      b = false;
    } else {
      dbgprintf("Strange Prediction Buffer!\n");
    }
    this-> k = pc % this->psize;
    this->y = this->perceptrons[k];
    for (int i = 0; i < this->wsize; ++i){
      int h = i % this->wsize;
      y += this->weights[k][i] * history[h];
      
    }
    if (this->y >=0) c = true;
    else c = false;
    if (a) ct++;
    else cf++;
    if (b) ct++;
    else cf++;
    if (c) ct++;
    else cf++;
    if (ct > cf) return true;
    else return false;
}
  break;
  case BPB: {
    PredictorState state = this->predbuf[pc % PRED_BUF_SIZE];
    if (state == STRONG_TAKEN || state == WEAK_TAKEN) {
      return true;
    } else if (state == STRONG_NOT_TAKEN || state == WEAK_NOT_TAKEN) {
      return false;
    } else {
      dbgprintf("Strange Prediction Buffer!\n");
    }   
  
  break;
}
  case SB:{
    return this->bit_state == BitState::TAKEN;
}
  break;
  case STB:{
    if (this->two_bit_state == ST || this->two_bit_state == WT){
       return true;
    } else if (this->two_bit_state == SNT || this->two_bit_state == WNT){
      return false;}
}
  break;
  default:
    dbgprintf("Unknown Branch Perdiction Strategy!\n");
    break;
  }
  return false;
}

void BranchPredictor::update(uint32_t pc, bool branch) {
  int id = pc % PRED_BUF_SIZE;
  PredictorState state = this->predbuf[id];
  if (branch) {
    this->bit_state = TAKEN;
    if (state == STRONG_NOT_TAKEN) {
      this->predbuf[id] = WEAK_NOT_TAKEN;
    } else if (state == WEAK_NOT_TAKEN) {
      this->predbuf[id] = WEAK_TAKEN;
    } else if (state == WEAK_TAKEN) {
      this->predbuf[id] = STRONG_TAKEN;
    } // do nothing if STRONG_TAKEN
    if (this->two_bit_state == SNT) {
      this->two_bit_state = WNT;
    } else if (this->two_bit_state == WNT) {
      this->two_bit_state = WT;
    } else if (this->two_bit_state == WT) {
      this->two_bit_state = ST;
    } // do nothing if STRONG_TAKEN

  } else { // not branch
   this->bit_state = NOT_TAKEN;
    if (state == STRONG_TAKEN) {
      this->predbuf[id] = WEAK_TAKEN;
    } else if (state == WEAK_TAKEN) {
      this->predbuf[id] = WEAK_NOT_TAKEN;
    } else if (state == WEAK_NOT_TAKEN) {
      this->predbuf[id] = STRONG_NOT_TAKEN;
    } // do noting if STRONG_NOT_TAKEN
    if (this->two_bit_state == ST) {
      this->two_bit_state = WT;
    } else if (this->two_bit_state == WT) {
      this->two_bit_state = WNT;
    } else if (this->two_bit_state == WNT) {
      this->two_bit_state = SNT;
    } // do noting if STRONG_NOT_TAKEN

  }
  int t = (branch) ? 1 : -1;
  int ws = 0;
  if (this->y / abs(this->y) != branch || abs(this->y) <= this->kTheta){
    
    ws = 1 << (this->weightsize - 1);
    int b = this->perceptrons[this->k] + t;
    if (abs(b) < ws){
      this->perceptrons[this->k] = b;
    }
    for (int i = 0; i < this->wsize; ++i){
      int h = i % this->wsize;
      int w = this->weights[this->k][i] + t * this->history[h];
      if (abs(w) < ws){
        this->weights[this->k][i] = w;
      }
    } 
  }
  this->history[this->hs] = t;
  this->hs = 1 % this->wsize;
}

std::string BranchPredictor::strategyName() {
  switch (this->strategy) {
  case NT:
    return "Always Not Taken";
  case AT:
    return "Always Taken";
  case BTFNT:
    return "Back Taken Forward Not Taken";
  case BPB:
    return "Branch Prediction Buffer";
  case RAND:
    return "Random";
  case SB:
    return "Saturating One Bit";
  case STB:
    return "Saturating Two Bits";
  case PP:
    return "Perceptron";
  case HP:
    return "Hybrid: Back Taken + Perceptron + Branch Prediction Buffer";
  default:
    dbgprintf("Unknown Branch Perdiction Strategy!\n");
    break;
  }
  return "error"; // should not go here
}
