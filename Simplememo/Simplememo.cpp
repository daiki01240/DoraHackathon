#include <stdio.h>
#include <string>
#include <eosiolib/eosio.hpp>

using namespace eosio;

class Simplememo : public contract {
  public:
      // constructor
      Simplememo(account_name s):contract(s), _memos(s, s) // ※4
      {}

      // @abi action
      void addmemo(std::string content1,std::string content2)
      {
        // update the table to include a new memo
        _memos.emplace(get_self(), [&](auto& p)
                                      {
                                        p.key = _memos.available_primary_key();
                                        p.content1 = content1;
                                        p.content2 = content2;
                                      });
      };

  private:
      // @abi table
      struct memo // ※1
      {
         uint64_t     key;
         std::string  content1;
         std::string  content2;

         uint64_t primary_key() const { return key; }
      };
      typedef eosio::multi_index<N(memo), memo> memos;  // ※2

      memos _memos; //※3
};

EOSIO_ABI( Simplememo, (addmemo))
