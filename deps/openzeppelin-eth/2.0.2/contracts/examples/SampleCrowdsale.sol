pragma solidity ^0.4.24;

import "deps/zos-lib/contracts/Initializable.sol";
import "../crowdsale/validation/CappedCrowdsale.sol";
import "../crowdsale/distribution/RefundableCrowdsale.sol";
import "../crowdsale/emission/MintedCrowdsale.sol";
import "../token/ERC20/ERC20Mintable.sol";


/**
 * @title SampleCrowdsaleToken
 * @dev Very simple ERC20 Token that can be minted.
 * It is meant to be used in a crowdsale contract.
 */
contract SampleCrowdsaleToken is Initializable, ERC20Mintable {

  string public name;
  string public symbol;
  uint8 public decimals;

  function initialize(address sender) public initializer {
    ERC20Mintable.initialize(sender);

    name = "Sample Crowdsale Token";
    symbol = "SCT";
    decimals = 18;
  }

  uint256[50] private ______gap;
}


/**
 * @title SampleCrowdsale
 * @dev This is an example of a fully fledged crowdsale.
 * The way to add new features to a base crowdsale is by multiple inheritance.
 * In this example we are providing following extensions:
 * CappedCrowdsale - sets a max boundary for raised funds
 * RefundableCrowdsale - set a min goal to be reached and returns funds if it's not met
 *
 * After adding multiple features it's good practice to run integration tests
 * to ensure that subcontracts works together as intended.
 */
// XXX There doesn't seem to be a way to split this line that keeps solium
// happy. See:
// https://github.com/duaraghav8/Solium/issues/205
// --elopio - 2018-05-10
// solium-disable-next-line max-len
contract SampleCrowdsale is Initializable, Crowdsale, CappedCrowdsale, RefundableCrowdsale, MintedCrowdsale {

  function initialize(
    uint256 openingTime,
    uint256 closingTime,
    uint256 rate,
    address wallet,
    uint256 cap,
    ERC20Mintable token,
    uint256 goal
  )
    public
    initializer
  {
    Crowdsale.initialize(rate, wallet, token);
    CappedCrowdsale.initialize(cap);
    TimedCrowdsale.initialize(openingTime, closingTime);
    RefundableCrowdsale.initialize(goal);

    //As goal needs to be met for a successful crowdsale
    //the value needs to less or equal than a cap which is limit for accepted funds
    require(goal <= cap);
  }

  uint256[50] private ______gap;
}
