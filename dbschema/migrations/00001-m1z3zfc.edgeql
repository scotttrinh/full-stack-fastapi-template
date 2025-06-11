CREATE MIGRATION m1z3zfcfsxselznj2f7cez6v5ste7dye5ea4lklnht4dok4coa7xgq
    ONTO initial
{
  CREATE EXTENSION pgcrypto VERSION '1.3';
  CREATE EXTENSION auth VERSION '1.0';
  CREATE FUTURE simple_scoping;
  CREATE TYPE default::User {
      CREATE REQUIRED LINK identity: ext::auth::Identity {
          ON SOURCE DELETE DELETE TARGET;
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE PROPERTY email: std::str {
          CREATE CONSTRAINT std::exclusive;
          CREATE CONSTRAINT std::max_len_value(255);
          CREATE CONSTRAINT std::min_len_value(1);
      };
      CREATE PROPERTY full_name: std::str {
          CREATE CONSTRAINT std::max_len_value(255);
          CREATE CONSTRAINT std::min_len_value(1);
      };
      CREATE REQUIRED PROPERTY is_superuser: std::bool {
          SET default := false;
      };
  };
  CREATE SINGLE GLOBAL default::current_user := (std::assert_single((SELECT
      default::User
  FILTER
      (.identity ?= GLOBAL ext::auth::ClientTokenIdentity)
  )));
  CREATE TYPE default::Item {
      CREATE REQUIRED LINK owner: default::User {
          ON TARGET DELETE DELETE SOURCE;
      };
      CREATE PROPERTY description: std::str {
          CREATE CONSTRAINT std::max_len_value(255);
          CREATE CONSTRAINT std::min_len_value(1);
      };
      CREATE PROPERTY title: std::str {
          CREATE CONSTRAINT std::max_len_value(255);
          CREATE CONSTRAINT std::min_len_value(1);
      };
  };
};
