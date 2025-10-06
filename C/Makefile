TARGETS=$(patsubst %.c,%,$(shell grep -rl "main" --include='[0-9]*_*.c' | tr '\n' ' '))

CYAN=\033[0;35m
GREEN=\033[0;32m
ORANGE=\033[0;33m
NC=\033[0m

RUN=0

.PHONY: all
all: $(TARGETS)
	@echo "$(ORANGE)LEETCODE SOLUTIONS IN C: $(words $(wildcard [0-9]*_*.c))$(NC) $(CYAN)RAN: $(RUN)$(NC)"

%.bin: %.c
	@$(CC) $(CFLAGS) $< -o $@

define add_target
.PHONY: $(1)
$(1): $(1).bin
	@echo "$(GREEN)RUNNING $(1).bin$(NC)"
	@./$(1).bin
	$(eval RUN=$(shell echo $$(($(RUN)+1))))
endef

$(foreach T,$(TARGETS),$(eval $(call add_target,$(T))))

.PHONY: run_and_clean
run_and_clean: all clean

.PHONY: clean
clean:
	@rm -f *.bin
